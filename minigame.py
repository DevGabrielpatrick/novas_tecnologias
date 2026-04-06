import pygame, sys, random

pygame.init()
TELA = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sobrevivência")
CLOCK = pygame.time.Clock()

fonte_grande = pygame.font.SysFont("Arial", 48, bold=True)
fonte_normal = pygame.font.SysFont("Arial", 28)

# =========================
# CLASSES
# =========================
class EntidadeBase:
    def __init__(self, x, y, largura, altura, cor):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def colidiu_com(self, outra):
        return self.rect.colliderect(outra.rect)

class Jogador(EntidadeBase):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, (0, 100, 255))
        self.velocidade = 5

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT] and self.rect.x < 750:
            self.rect.x += self.velocidade
        if teclas[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_DOWN] and self.rect.y < 550:
            self.rect.y += self.velocidade

class Inimigo(EntidadeBase):
    def __init__(self, x, y, velocidade=3):
        super().__init__(x, y, 40, 40, (255, 150, 0))
        self.velocidade = velocidade
        self.vida = 3

    def perseguir(self, alvo):
        if self.rect.x < alvo.rect.x: self.rect.x += self.velocidade
        if self.rect.x > alvo.rect.x: self.rect.x -= self.velocidade
        if self.rect.y < alvo.rect.y: self.rect.y += self.velocidade
        if self.rect.y > alvo.rect.y: self.rect.y -= self.velocidade

class InimigoRapido(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=6)
        self.cor = (0, 255, 255)

class InimigoGigante(Inimigo):
    def __init__(self, x, y):
        super().__init__(x, y, velocidade=2)
        self.rect = pygame.Rect(x, y, 80, 80)
        self.cor = (150, 0, 150)
        self.vida = 5

class Projetil(EntidadeBase):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 10, (255, 255, 0))
        self.velocidade = -8

    def mover(self):
        self.rect.y += self.velocidade

# =========================
# HUD
# =========================
def desenhar_hud(tela, estado):
    texto_pont = fonte_normal.render(f"Pontuação: {estado['pontuacao']}", True, (255, 255, 255))
    texto_vidas = fonte_normal.render(f"Vidas: {estado['vidas']}", True, (255, 100, 100))

    tela.blit(texto_pont, (10, 10))
    tela.blit(texto_vidas, (10, 40))

def desenhar_game_over(tela):
    overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    tela.blit(overlay, (0, 0))
    texto = fonte_grande.render("GAME OVER", True, (255, 60, 60))
    tela.blit(texto, texto.get_rect(center=(400, 300)))

# =========================
# CONFIG INICIAL
# =========================
jogador = Jogador(375, 275)

inimigos = []
for _ in range(3):
    inimigos.append(Inimigo(random.randint(0, 750), 0))
for _ in range(2):
    inimigos.append(InimigoRapido(random.randint(0, 750), 0))
for _ in range(1):
    inimigos.append(InimigoGigante(random.randint(0, 750), 0))

projeteis = []

estado = {"pontuacao": 0, "vidas": 5, "rodando": True}

timer_spawn = 0

niveis = {
    1: {"vel": 2, "qtd": 4},
    2: {"vel": 3, "qtd": 6},
    3: {"vel": 4, "qtd": 8}
}

nivel_atual = 1
tempo_msg = 0

while estado["rodando"]:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                projeteis.append(Projetil(jogador.rect.centerx, jogador.rect.y))

    # Atualização
    teclas = pygame.key.get_pressed()
    jogador.mover(teclas)

    # Projetéis
    for p in projeteis[:]:
        p.mover()
        if p.rect.y < 0:
            projeteis.remove(p)

    # Inimigos
    for ini in inimigos[:]:
        ini.perseguir(jogador)

        # Colisão jogador
        if jogador.colidiu_com(ini):
            estado["vidas"] -= 1
            ini.rect.topleft = (random.randint(0, 750), 0)

            if estado["vidas"] <= 0:
                estado["rodando"] = False

        # Colisão projétil
        for p in projeteis[:]:
            if p.colidiu_com(ini):
                ini.vida -= 1

                if ini.vida <= 0:
                    inimigos.remove(ini)

                if p in projeteis:
                    projeteis.remove(p)
                break

    # Spawn
    timer_spawn += 1
    if timer_spawn % 300 == 0:
        tipo = random.choice([Inimigo, InimigoRapido, InimigoGigante])
        inimigos.append(tipo(random.randint(0, 750), 0))
        estado["pontuacao"] += 50

    # Pontuação
    estado["pontuacao"] += 1

    # Sistema de níveis
    if estado["pontuacao"] % 500 == 0:
        nivel_atual = min(nivel_atual + 1, 3)
        tempo_msg = pygame.time.get_ticks()

        inimigos.clear()
        for _ in range(niveis[nivel_atual]["qtd"]):
            inimigos.append(Inimigo(random.randint(0, 750), 0, niveis[nivel_atual]["vel"]))

    # Render
    TELA.fill((20, 20, 40))

    jogador.desenhar(TELA)

    for ini in inimigos:
        ini.desenhar(TELA)

    for p in projeteis:
        p.desenhar(TELA)

    desenhar_hud(TELA, estado)

    # Mensagem de nível
    if pygame.time.get_ticks() - tempo_msg < 2000:
        msg = fonte_normal.render(f"Nível {nivel_atual}", True, (255,255,255))
        TELA.blit(msg, (350, 50))

    pygame.display.flip()
    CLOCK.tick(60)

# Game Over
desenhar_game_over(TELA)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()