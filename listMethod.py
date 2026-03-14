l1 = ['a', 'b']

print(f"l1 = {l1},, len of l1 = {len(l1)}")

print('-'*10)

l1.append('c')

print(f"l1 after append = {l1}, len of l1 = {len(l1)}")

l2 = l1
print('-'*10)

print(f'l2 = l1 and then l2 = {l2}, len 12 = {len(l2)}')

print('-'*10)

l2.clear()

print(f'l2 after clear = {12} , len l2 = {len(l2)}')
print(f'l1 after clear on l2 = {l1}, len l1 = {len(l1)}')
print(f'l1 after clear on l2 = {l1}, len l1 = {len(l1)}')

print('now we init value ')

print()

l1 = ['arc','da25']
print(f"l1 = {l1},, len of l1 = {len(l1)}")
print('-'*10)

l2 = l1.copy()

print(f"l2 = {l2},, len of l2 = {len(l2)}")

print('-'*10)

l2.clear()

print(f'l2 = after clear = {l2} , len l2 = {len(l2)}')
print(f'l1 after clear on l2 = {l1} , len l1 = {len(l1)}')


l2.append(['a','c'])


print(f'l2 after clear = {l2} , len 12 = {len(12)}')

l2.clear()
print('-'*10)
print(f'l2 after clear = {l2} , len l2 = {len(12)}')
print('-'*10)

l2.extend(['a','c'])

print(f'l2 after extend [a,b] = {l2} , len l2 = {len(l2)}')
