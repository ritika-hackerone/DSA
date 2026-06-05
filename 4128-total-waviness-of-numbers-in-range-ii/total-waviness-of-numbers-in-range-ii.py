from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1, length):
                """
                Returns:
                    (count_numbers, total_waviness)
                """
                if pos == m:
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_wave = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # still leading zeros
                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            10,   # dummy
                            10,   # dummy
                            0
                        )
                        total_count += cnt
                        total_wave += wav

                    else:
                        if not started:
                            # first significant digit
                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                10,  # no second-last yet
                                d,
                                1
                            )
                            total_count += cnt
                            total_wave += wav

                        else:
                            add = 0

                            # If we already have at least 2 digits,
                            # prev1 becomes the middle digit of:
                            # prev2, prev1, d
                            if length >= 2:
                                if (prev1 > prev2 and prev1 > d) or \
                                   (prev1 < prev2 and prev1 < d):
                                    add = 1

                            cnt, wav = dp(
                                pos + 1,
                                ntight,
                                True,
                                prev1,
                                d,
                                length + 1
                            )

                            total_count += cnt
                            total_wave += wav + add * cnt

                return (total_count, total_wave)

            return dp(0, True, False, 10, 10, 0)[1]

        return solve(num2) - solve(num1 - 1)