import random


def load_data() :
        words1 = []
        hints1 = []
        words2 = []
        hints2 = []

        file1 = open('famous_actors.txt', 'r')
        for idx, line in enumerate(file1):
                if idx%2==0 : words1.append(line.strip())
                else : hints1.append(line.strip()) 
        file1.close()

        file2 = open('famous_songs.txt', 'r')
        for idx, line in enumerate(file2):
                if idx%2==0 : words2.append(line.strip())
                else : hints2.append(line.strip()) 
        file2.close()
                        
        return [words1, words2], [hints1, hints2]

def play_word(word, hint, score) :
        
        board = [c if not(c.isalpha()) else '_' for c in word ]
        wrong = []
        right = []
        rmn = 8

        print('\nHint: ',hint)

        while(rmn) :
                if(''.join(board) == word) : break

                print('\n', ' '.join(board), ' score ', score,',remaining wrong guess ', 
                rmn, ',wrong guessed: ', ','.join(wrong))
                c = input('>')

                if len(c) != 1 or not c.isalpha(): 
                        print('\nYou can only answer one alphabet.')
                        continue

                if c.lower() in right : 
                        print('\nYou\'ve answered it.' )
                        continue
                
                

                found = []
                for idx,w in enumerate(word.lower()) : 
                        if c==w : found.append(idx)

                if len(found)!=0 : 
                        right.append(c.lower())
                        for i in found :
                                board[i] = word[i]
                        score += 15
                else : 
                        wrong.append(c) 
                        score -= 5
                        rmn-=1
                
                

        if (rmn == 0) : print('\n\nYou\'re worng!!\nThe answer is ',word)
        else : print('\n\nWin!!')

        return score

def start(words, hints) :
        score = 0

        while(1) :

                idx = random.randint(0,len(words))
                word = words[idx-1]
                hint = hints[idx-1]
                words.remove(word)
                hints.remove(hint)
                score = play_word(word, hint, score)
                print('Your score is',score)

                if len(words) == 0 :
                        return score

                while(1) :
                        print('\n\nDo you want to KEEP PLAYING ? [y/n]')
                        a = input()
                        if a.lower() == 'n' : return False
                        elif a.lower() == 'y' : break
                        else : print('\nInvalid input')
                
        return True
                

def main() :

        word_data, hint_data = load_data()

        while(1) :

                print('\n\n\nHANGMAN\n')
                print('Select Category:\n1: Famous Actors\n2: Famous Songs')
                x = input('>')

                if x!='1' and x!='2' : 
                        print('\nInvalid input')
                        continue

                
                finish = start(word_data[int(x)-1], hint_data[int(x)-1])
                if finish : print('\nYou\'ve cleared all words.')

                while(1) :
                        print('\n\nDo you want to exit? [y/n]')
                        a = input()
                        if a.lower() == 'y' : exit(0)
                        elif a.lower() == 'n' : break
                        else : print('\nInvalid input')
                

main()