# ！/usr/bin/env python3
# -*- coding: utf-8 -*-
# 强制Python输出编码为UTF-8（解决Windows Git Bash中文乱码）
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# test_order.py - 订单自动化测试脚本（彻底解决中文乱码）
# 模拟电商平台的订单创建、支付、查询功能

# 1. 模拟用户信息和商品信息
user_info = {
    "user_id": 1001,
    "username": "test_user",
    "address": "北京市朝阳区测试路1号"
}

product_info = {
    "product_id": 2001,
    "product_name": "测试手机",
    "price": 2999.99,
    "count": 1  # 购买数量
}

# 2. 定义订单创建函数
def create_order(user, product):
    """创建订单"""
    try:
        # 模拟生成订单号（时间戳+用户ID）
        import time
        order_id = f"ORD{int(time.time())}{user['user_id']}"
        
        # 计算订单总金额
        total_amount = product["price"] * product["count"]
        
        # 构造订单信息
        order = {
            "order_id": order_id,
            "user_id": user["user_id"],
            "product_id": product["product_id"],
            "total_amount": total_amount,
            "status": "待支付",  # 订单初始状态
            "create_time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        # 纯文字输出，适配所有终端
        print(f"【成功】订单创建成功！订单号：{order_id}")
        return order
    except Exception as e:
        print(f"【失败】订单创建失败：{str(e)}")
        return None

# 3. 定义订单支付函数
def pay_order(order):
    """模拟订单支付"""
    if not order:
        return False
    try:
        # 模拟支付成功（测试场景下固定返回成功）
        import time  # 补充导入time
        order["status"] = "已支付"
        order["pay_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"【成功】订单支付成功！订单号：{order['order_id']}")
        return True
    except Exception as e:
        print(f"【失败】订单支付失败：{str(e)}")
        return False

# 4. 定义订单查询函数
def query_order(order_id):
    """模拟查询订单"""
    # 测试场景下，直接返回模拟的订单信息
    mock_order = {
        "order_id": order_id,
        "status": "已支付",
        "total_amount": 2999.99
    }
    print(f"【成功】订单查询成功！订单信息：{mock_order}")
    return mock_order

# 5. 执行订单测试流程（测试用例核心）
if __name__ == "__main__":
    print("===== 开始执行订单自动化测试 =====")
    
    # 步骤1：创建订单
    new_order = create_order(user_info, product_info)
    
    # 步骤2：支付订单（断言校验）
    assert new_order is not None, "订单创建失败，无法执行支付"
    pay_result = pay_order(new_order)
    assert pay_result is True, "订单支付失败"
    
    # 步骤3：查询订单（断言校验）
    order_detail = query_order(new_order["order_id"])
    assert order_detail["status"] == "已支付", "订单状态异常，支付后未更新为已支付"
    
    print("===== 订单自动化测试全部通过！=====")