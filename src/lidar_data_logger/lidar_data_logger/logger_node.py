#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import os
import csv
from datetime import datetime

class LidarDataLogger(Node):
    def __init__(self):
        super().__init__('lidar_data_logger')
        
        # Параметры (можно задать через launch-файл или командную строку)
        self.declare_parameter('topic', '/lidar/scan')
        self.declare_parameter('file_path', 'lidar_data.csv')
        self.declare_parameter('max_records', 1000)  # записать только первые N сканов (0 = бесконечно)
        
        topic = self.get_parameter('topic').value
        file_path = self.get_parameter('file_path').value
        self.max_records = self.get_parameter('max_records').value
        
        # Подписка на топик лидара
        self.subscription = self.create_subscription(
            LaserScan,
            topic,
            self.scan_callback,
            10  # очередь
        )
        self.subscription  # предотвращаем удаление
        
        # Открываем файл для записи (CSV)
        self.file = open(file_path, 'w', newline='')
        self.writer = csv.writer(self.file)
        # Заголовок: время, количество точек, все дистанции
        header = ['timestamp_sec', 'timestamp_nanosec', 'num_ranges'] + [f'range_{i}' for i in range(360)]
        self.writer.writerow(header)
        
        self.record_count = 0
        self.get_logger().info(f'Lidar logger started. Writing to {file_path}')
        self.get_logger().info(f'Max records: {self.max_records if self.max_records>0 else "infinite"}')

    def scan_callback(self, msg):
        # Проверка лимита записей
        if self.max_records > 0 and self.record_count >= self.max_records:
            self.get_logger().info('Max records reached, stopping subscription.')
            self.destroy_subscription(self.subscription)
            self.file.close()
            return
        
        # Формируем строку: время + все дальности
        row = [
            msg.header.stamp.sec,
            msg.header.stamp.nanosec,
            len(msg.ranges)
        ]
        row.extend(msg.ranges)  # добавляем все значения дальности
        
        # Записываем в CSV
        self.writer.writerow(row)
        self.file.flush()  # немедленно сбрасываем на диск (чтобы не потерять при аварии)
        
        self.record_count += 1
        if self.record_count % 100 == 0:
            self.get_logger().info(f'Recorded {self.record_count} scans')

    def __del__(self):
        if hasattr(self, 'file'):
            self.file.close()

def main(args=None):
    rclpy.init(args=args)
    node = LidarDataLogger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down logger...')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()