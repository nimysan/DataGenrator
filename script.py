import csv
import string
import random
import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='生成CSV数据')

# 添加需要的参数
parser.add_argument('filename', type=str, help='生成的CSV文件名')
parser.add_argument('num_rows', type=int, help='生成的行数')

# 解析命令行参数
args = parser.parse_args()

# 获取参数的值
filename = args.filename
num_rows = args.num_rows

# 在这里使用filename和num_rows参数进行处理
print(f"生成文件名: {filename}")
print(f"生成行数: {num_rows}")


def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'age', 'email', 'desc'])

        batch_size = 1000  # 每次写入的行数
        rows = []

        for i in range(num_rows):
            id = i + 1
            name = ''.join(random.choices(string.ascii_uppercase, k=10))
            age = random.randint(18, 60)
            email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@aws-example.com"
            desc = ''.join(random.choices(string.ascii_letters, k=400))
            rows.append([id, name, age, email, desc])

            if len(rows) >= batch_size:
                writer.writerows(rows)
                rows = []

        if rows:
            writer.writerows(rows)


# 调用函数生成CSV文件
generate_csv(filename, num_rows)
