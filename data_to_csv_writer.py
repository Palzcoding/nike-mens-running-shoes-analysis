import re
import csv

# 读取 data.txt 文件
with open("data.txt", "r", encoding="utf-8") as f:
    raw_data = f.read()

# 预处理：将单引号转换为双引号，确保 JSON 格式合法
raw_data = raw_data.replace("'", '"')

# 匹配产品信息（使用更宽松的匹配规则）
product_pattern = re.compile(
    r'"name":\s*"(.*?)".*?"brand":\s*"(.*?)".*?"currentPrice":\s*([\d.]+).*?"fullPrice":\s*([\d.]+).*?"category":\s*"(.*?)".*?"color":\s*"(.*?)".*?"skuData":\s*\[(.*?)\]', 
    re.DOTALL
)

# 匹配 SKU 数据
sku_pattern = re.compile(r'"size":\s*"(.*?)".*?"sku":\s*"(.*?)".*?"gtin":\s*"(.*?)"', re.DOTALL)

# 存储提取的数据
extracted_data = []

for product in product_pattern.findall(raw_data):
    name, brand, current_price, full_price, category, color, sku_data = product
    
    # 匹配 SKU 详情
    skus = sku_pattern.findall(sku_data)
    
    for size, sku, gtin in skus:
        extracted_data.append([name, brand, current_price, full_price, category, color, size, sku, gtin])

# 写入 CSV 文件
csv_filename = "nike_products.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Brand", "Current Price", "Full Price", "Category", "Color", "Size", "SKU", "GTIN"])
    writer.writerows(extracted_data)

print(f"数据已成功提取并保存到 {csv_filename}，共 {len(extracted_data)} 条记录！")
