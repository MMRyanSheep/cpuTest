import pygame, random
SCREEN_W, SCREEN_H = 1920, 1080
def quick_sort(btm, top):  
    global L
    if btm >= top:
        return
    btm0, top0 = btm, top
    key = btm
    flag = True
    while btm < top:
        while L[top] > L[key]:
            top -= 1
            if btm == top:
                flag = False
                break
        if not flag:
            break
        L[top], L[key] = L[key], L[top]
        pygame.draw.rect(screen, (255, 0, 0), (key * 3, 0, 4, SCREEN_H), 0)
        pygame.draw.rect(screen, (255, 255, 255), (key * 3, SCREEN_H - L[key] * 2, 4, L[key] * 2), 0)
        pygame.draw.rect(screen, (255, 0, 0), (top * 3, SCREEN_H - L[top] * 2, 4, L[top] * 2), 0)
        pygame.event.get()
        pygame.display.update()
        key = top
        while L[btm] < L[key]:
            btm += 1
            if btm == top:
                flag = False
                break
        if not flag:
            break
        L[btm], L[key] = L[key], L[btm]
        pygame.draw.rect(screen, (0, 0, 0), (btm * 3, 0, 4, SCREEN_H), 0)
        pygame.draw.rect(screen, (255, 255, 255), (key * 3, SCREEN_H - L[key] * 2, 4, L[key] * 2), 0)
        pygame.draw.rect(screen, (255, 0, 0), (btm * 3, SCREEN_H - L[btm] * 2, 4, L[btm] * 2), 0)
        pygame.display.update()
        key = btm
    pygame.draw.rect(screen, (255, 255, 255), (key * 3, SCREEN_H - L[key] * 2, 4, L[key] * 2), 0)
    quick_sort(btm0, key - 1)
    quick_sort(key + 1, top0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H)) 
L = list(range(1, 1080))
random.shuffle(L)

screen.fill((0, 0, 0))
key = 0
for i in range(len(L)):
    if i == key:
        c = (255, 0, 0)
    else:
        c = (255, 255, 255)
    pygame.draw.rect(screen, c, (i * 3, SCREEN_H - L[i] * 2, 4, L[i] * 2), 0)
    pygame.display.update()