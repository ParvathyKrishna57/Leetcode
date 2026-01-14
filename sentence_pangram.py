class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha="abcdefghijklmnopqrstuivwxyz"
        for ch in alpha:
            if ch not in sentence:
                return False
        return True