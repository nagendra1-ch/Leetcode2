class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        n=purchaseAmount%10
        num=purchaseAmount
        if n<5:
            num=num-n
        if n>=5:
            num+=(10-n)
        return 100-num
