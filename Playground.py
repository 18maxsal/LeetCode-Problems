
def test(word: str, target1: str, target2: str):

    ans = float('inf')
    target1_index = -1
    target2_index = -1

    for index, curr_word in enumerate(word):

        if curr_word == target1:
            target1_index = index
            if target1_index > -1 and target2_index > -1:
                ans = min(ans, abs(target1_index - target2_index))
        
        elif curr_word == target2:
            target2_index = index
            if target1_index > -1 and target2_index > -1:
                ans = min(ans, abs(target1_index - target2_index))
    
    return ans


word = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
target1 = "fox"
target2 = "dog"

print(test(word, target1, target2))