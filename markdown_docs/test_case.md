## ClassDef BankAccount
**BankAccount**: BankAccount的功能是管理银行账户的相关操作。
**attributes**:
· owner: 账户所有者
· balance: 账户余额
**Code Description**:
BankAccount类具有以下方法：
- \__init\__(self, owner, balance=0)：初始化银行账户，设置账户所有者和初始余额（默认为0）。
- deposit(self, amount)：存款操作，如果存款金额大于0，则增加余额并显示新余额；否则提示存款金额必须为正数。
- withdraw(self, amount)：取款操作，如果取款金额大于0且小于等于余额，则减少余额并显示新余额；否则提示余额不足或取款金额无效。
- get_balance(self) -> float：获取当前余额。
- display_account_info(self)：显示账户信息，包括账户所有者和余额。
**Note**: 在使用withdraw方法时，需注意取款金额必须大于0且不超过当前余额。
**Output Example**:
Owner: Alice
Balance: 1000.0
### FunctionDef __init__(self, owner, balance)
**__init__**: __init__函数的功能是初始化一个BankAccount对象。

**参数**:
· owner: 表示银行账户的所有者。
· balance: 表示银行账户的余额，默认值为0。

**代码描述**:
__init__函数是一个构造函数，用于初始化BankAccount对象的属性。在函数内部，将传入的owner参数赋值给对象的owner属性，将传入的balance参数赋值给对象的balance属性。如果未提供balance参数，则默认余额为0。

**注意**: 在创建BankAccount对象时，需要传入owner参数，可选择性地传入balance参数。
***
### FunctionDef deposit(self, amount)
**deposit**: deposit函数的功能是存款。

**parameters**:
· amount: 存款金额，必须为正数。

**Code Description**:
deposit函数接受一个参数amount，用于存入银行账户。如果amount大于0，将会将amount加到账户余额上，并打印出存款金额和新的余额；如果amount小于等于0，将会打印出"存款金额必须为正数"的提示信息。

**Note**:
- 在调用deposit函数时，确保传入的存款金额为正数，否则将无法成功存款。
***
### FunctionDef withdraw(self, amount)
**withdraw**: withdraw函数的功能是从银行账户中提取指定金额的资金。

**parameters**:
· amount: 表示要提取的金额。

**Code Description**:
该函数首先检查提取金额是否大于0且不超过账户余额。如果条件满足，将从账户余额中扣除提取金额，并打印出提取金额和新的账户余额。如果条件不满足，将打印出"资金不足或金额无效"的提示信息。

**Note**:
请确保提取金额大于0且不超过账户余额，否则将无法成功提取资金。

**Output Example**:
如果提取成功，返回True；如果提取失败，返回False。
***
### FunctionDef get_balance(self)
**get_balance**: get_balance函数的功能是返回当前银行账户的余额。
**参数**：该函数无参数。
**代码描述**：该函数通过返回self.balance来获取当前银行账户的余额。
**注意**：在调用该函数之前，确保已经初始化了银行账户的余额。
**输出示例**：假设当前银行账户的余额为1000.0，则调用get_balance函数将返回1000.0。
***
### FunctionDef display_account_info(self)
**display_account_info**: display_account_info函数的作用是打印账户所有者和余额信息。
**参数**: 该函数无参数。
**代码描述**: display_account_info函数通过使用self.owner和self.balance打印出账户所有者和余额信息。
**注意**: 在调用display_account_info函数时，确保已经设置了owner和balance属性的值，以便正确显示账户信息。
***
