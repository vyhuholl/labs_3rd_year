#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import log10
from random import shuffle, sample
from numpy import inf


def decrypt(text, key):
    result = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for i in text:
        caps = False
        if i != i.lower():
            caps = True
        if i.lower() in alphabet:
            idx = alphabet.index(i.lower())
            if caps == True:
                result += key[idx].upper()
            else:
                result += key[idx]
        else:
            result += i
    return result


class Scorer:
    
    def __init__(self, freq_dict):
        #transforming a txt file to a python dictionary
        self.quadgrams = {}
        freq = open(freq_dict, 'r')
        for line in freq:
            word, frequency = line.split(' ')
            self.quadgrams[word] = int(frequency)
        freq.close()
        self.N = sum(self.quadgrams.values())
        #calculating log probabilities
        for key in self.quadgrams.keys():
            self.quadgrams[key] = log10(float(self.quadgrams[key])/self.N)
        self.floor = log10(0.01/self.N)
    
    def score(self, text):
        score = 0
        quadgrams = self.quadgrams.__getitem__
        text = text.split(' ')
        for word in text:
            word = word.upper()
            word = word.strip('.,:;""-')
        text = ''.join(text)
        for i in range(len(text) - 4 + 1):
            if text[i:i + 4] in self.quadgrams:
                score += quadgrams(text[i:i + 4])
            else:
                score += self.floor          
        return score


class Decoder():
    
    def __init__(self, score_func):
        self.encryption_ = ''
        self.decryption_ = ''
        self.score_func = score_func
        self.score_ = -inf
    
    def fit(self, text, num_trials = 30, num_swaps = 10 ** 4):
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        best_score = -inf
        for i in range(num_trials):
            shuffle(alphabet)
            key = alphabet
            best_trial_score = -inf
            for j in range(num_swaps):
                new_key = key
                i_1, i_2 = sample(range(26), 2)
                new_key[i_1], new_key[i_2] = new_key[i_2], new_key[i_1]
                decrypted_text = decrypt(text, new_key)
                score = self.score_func.score(decrypted_text)
                if score > best_trial_score:
                    key = new_key
                    best_trial_score = score
            if best_trial_score > best_score:
                best_key = new_key
                best_score = best_trial_score
        self.score_ = best_score
        self.decryption_ = ''.join(best_key)
        alphabet = list('abcdefghijklmnopqrstuvwxyz')
        for i in range(26):
            idx = self.decryption_.index(alphabet[i])
            self.encryption_ += alphabet[idx]
            
    
    def transform(self, text):
        return decrypt(text, self.decryption_)
    
    def inverse_transform(self, text):
        return decrypt(text, self.encryption_)


if __name__ == '__main__':
    pass
