def solution(s):
    def check(given_string):
        stack = []
        for ch in given_string:
            if ch == "(":
                stack.append(ch)
            else:
                if not stack or stack.pop() == ch:
                    return False
        if stack:
            return False
        return True

    def split(given_string):
        left = 0
        right = 0
        for i, ch in enumerate(given_string):
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                return (given_string[:i+1], given_string[i+1:])

    def inverse(given_string):
        ret = ""
        for ch in given_string:
            if ch == "(":
                ret += ")"
            else:
                ret += "("
        return ret

    def helper(given_string):
        if len(given_string) == 0:
            return ""

        if check(given_string):
            return given_string
        u, v = split(given_string)
        if check(u):
            return u + helper(v)

        return "(" + helper(v) + ")" + inverse(u[1:-1])

    return helper(s)
