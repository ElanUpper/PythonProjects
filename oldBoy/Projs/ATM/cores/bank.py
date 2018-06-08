# author: elan

class bank_account:

    def __init__(self, id):
        self.id = id ;
        self.account = 0 ;
        self.session_id = '' ;

    #----------------- 查询区域  ----------------
    # 验证用户有效性
    def verify_user(self, id):
        pass

    # 获取用户账户余额
    def get_user_amount(self, id):
        pass

    # 获取用户消费记录
    def get_user_transaction(self, id):
        pass


    #----------------- 操纵区域  ----------------
    # 用户充值
    # 参数 输入用户id
    # 返回值
    #        0 操作正常
    #       -1 用户无效
    def account_recharge_money(self, id):
        # 如果用户有效
        if not verify_user(id) :
            pass
        else :
            return 0 ;



    def account_transfer_account(self, amount):
        # 检查用户是否有这么多钱

        # 验证对方账户有效性

        # 自己账户扣款

        # 对方账户增加款项
        pass


