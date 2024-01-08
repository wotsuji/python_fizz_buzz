# Python FizzBuzz 2024年1月5日版


# 値オブジェクトクラス
class FizzBuzzSetting:
    # コンストラクタ
    def __init__(self, fizz_str="fizz", fizz_count=3, buzz_str="buzz", buzz_count=5):
        self.fizz_str = fizz_str
        self.fizz_count = fizz_count
        self.buzz_str = buzz_str
        self.buzz_count = buzz_count

    # デバッグ
    def debugPrint(self):
        print("fizz_str:", self.fizz_str)
        print("fizz_count:", self.fizz_count)
        print("buzz_str:", self.buzz_str)
        print("buzz_count:", self.buzz_count)


# FizzBuzzクラス
class FizzBuzz:
    # コンストラクタ
    def __init__(self, o_fizz_buzz_setting):
        self.s = o_fizz_buzz_setting

    # Judge
    def judge(self, counter_i, judge_i, fizzbuzz_str):
        return_str = ""
        if counter_i % judge_i == 0:
            return_str += fizzbuzz_str
        return return_str

    # 実行
    def exec(self, start=1, end=100):
        fizzbuzz_results = []
        i = start
        end_i = end
        while i <= end_i:
            fizzbuzz_str = ""
            fizzbuzz_str += self.judge(i, self.s.fizz_count, self.s.fizz_str)
            fizzbuzz_str += self.judge(i, self.s.buzz_count, self.s.buzz_str)
            fizzbuzz_results.append({i: fizzbuzz_str})
            i = i + 1
        return fizzbuzz_results


# メイン処理
def main():
    # 設定
    dic = {}
    # 設定変更：fizz:3 buzz:5
    # dic = {"fizz_str": "fizz", "fizz_count": 3, "buzz_str": "buzz", "buzz_count": 5}
    # 値オブジェクト取得
    o_fizz_buzz_setting = FizzBuzzSetting(**dic)
    # fizzbuzzインスタンス化
    o_fizzbuzz = FizzBuzz(o_fizz_buzz_setting)
    # fizzbuzz実行
    fizzbuzz_results = o_fizzbuzz.exec(1, 100)
    # 出力
    for k in fizzbuzz_results:
        print(k)


if __name__ == "__main__":
    main()

