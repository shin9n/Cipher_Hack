def makeCodebook():
    # 복호화를 위한 사전과 암호화를 위한 사전을 만든다.
    decbook = {'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m',\
        '*':'n', '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '}
    
    # 암호화 사전은 복호화 사전의 키와 값을 뒤집어서 만든다.
    encbook = {}
    for k in decbook:
        val = decbook[k]
        
        # encbook[val] = k는 encbook['a'] = '5'라는 뜻 즉, 평문 a를 넣으면 암호문 5를 얻도록 저장    
        encbook[val] = k 
        
    return encbook, decbook
    
def encrypt(msg, encbook):
    for c in msg:
        if c in encbook:
            msg = msg.replace(c, encbook[c])
    return msg

def decrypt(msg, decbook):
    for c in msg:
        if c in decbook:
            msg = msg.replace(c, decbook[c])
            
    return msg

if __name__ == '__main__': # --> C/C++같은 언어의 main() 함수와 비슷한 역할, 여러개 있을 수 있다.
    plaintext = 'I love you with all my heart'
    
    encbook, decbook = makeCodebook()
    ciphertext = encrypt(plaintext, encbook)
    print(ciphertext)
    
    deciphertext = decrypt(ciphertext, decbook)
    print(deciphertext)
    
    