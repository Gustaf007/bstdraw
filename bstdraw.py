import sys
import pygame
import BST

pygame.init()
pygame.font.init()
black = 0, 0, 0
white = 255, 255, 255
font = pygame.font.Font(None, 26)

def drawBST(bst: BST.BST, tilesize=60):
    
    def getnodewidth(node: BST.BST.Node) -> int:
        if node is None:
            return 0
        return 1 + getnodewidth(node.left) + getnodewidth(node.right)
    
    def getnodeheight(node: BST.BST.Node) -> int:
        if node is None:
            return 0
        return max(getnodeheight(node.left) + 1, getnodeheight(node.right) + 1)
    
    def drawNode(node: BST.BST.Node, y, x):
        if node is None:
            return
        pixelpos = (x * tilesize, y * tilesize)
        pygame.draw.circle(screen, black, pixelpos, 21)
        #calculate x-position of left child
        lx = x - getnodewidth(node.left) + getnodewidth(None if node.left is None else node.left.left)
        #calculate x-position of right child
        rx = x + 1 + getnodewidth(None if node.right is None else node.right.left)
        #draw left and right branches
        if not node.left is None:
            pygame.draw.line(screen, black, pixelpos, (lx * tilesize, (y + 1) * tilesize), 2)
        if not node.right is None:
            pygame.draw.line(screen, black, pixelpos, (rx * tilesize, (y + 1) * tilesize), 2)
        #draw node and the key
        pygame.draw.circle(screen, white, pixelpos, 19)
        text = font.render(str(node.key), 1, black)
        textpos = text.get_rect(centerx=x * tilesize, centery=y * tilesize)
        screen.blit(text, textpos)
        #recursively draw left and right child of current node.
        drawNode(node.left, y + 1, lx)
        drawNode(node.right, y + 1, rx)
    
    
    node = bst.root
    size = width, height = (getnodewidth(node)+1) * tilesize, (getnodeheight(node)+1) * tilesize
    screen = pygame.display.set_mode(size)
    screen.fill(white)

    drawNode(node, 1, getnodewidth(node.left) + 1)
    pygame.display.flip()


bst = BST.BST()
bst.put("E", 1)
bst.put("A", 2)
bst.put("C", 3)
bst.put("S", 4)
bst.put("I", 5)
bst.put("H", 6)
bst.put("Q", 7)
bst.put("N", 8)
bst.put("R", 9)
bst.put("X", 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    drawBST(bst)
