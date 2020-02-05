"""
Autor: Pierre Vieira
Data da submissão: 05/02/2020 18:08:21
"""
for c in range(int(input())):
    s1 = input()
    s2 = input()
    s3 = input()
    if s1[s3.find('_')] == s2[s3.rfind('_')] or s2[s3.find('_')] == s1[s3.rfind('_')]:
        print('Y')
    else:
        print('N')
