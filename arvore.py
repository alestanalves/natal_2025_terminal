#!/usr/bin/env python3

import os
import time
import random
import sys

# Cores ANSI
RESET = "\033[0m"
VERDE = "\033[92m"
VERDE_ESCURO = "\033[32m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIANO = "\033[96m"
BRANCO = "\033[97m"
DOURADO = "\033[33m"
BOLD = "\033[1m"

# Enfeites coloridos
ENFEITES = [
    (VERMELHO, "●"),
    (AMARELO, "●"),
    (AZUL, "●"),
    (MAGENTA, "●"),
    (CIANO, "●"),
    (DOURADO, "★"),
]

LUZES = [
    (VERMELHO, "◆"),
    (AMARELO, "◆"),
    (AZUL, "◆"),
    (MAGENTA, "◆"),
    (CIANO, "◆"),
    (BRANCO, "✦"),
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def esconder_cursor():
    print("\033[?25l", end="")

def mostrar_cursor():
    print("\033[?25h", end="")

# Árvore de Natal base
ARVORE = [
    "         ★         ",
    "         █         ",
    "        /█\\        ",
    "       /███\\       ",
    "      /█████\\      ",
    "     /███████\\     ",
    "    /█████████\\    ",
    "      /█████\\      ",
    "     /███████\\     ",
    "    /█████████\\    ",
    "   /███████████\\   ",
    "  /█████████████\\  ",
    "     /███████\\     ",
    "    /█████████\\    ",
    "   /███████████\\   ",
    "  /█████████████\\  ",
    " /███████████████\\ ",
    "/█████████████████\\",
    "       ████        ",
    "       ████        ",
    "    ▀▀▀████▀▀▀     ",
]

# Mensagem "Feliz Natal"
FELIZ_NATAL = [
    "",
    "",
    f"  {BOLD}{VERMELHO}╔═══════════════════╗{RESET}",
    f"  {BOLD}{VERMELHO}║                   ║{RESET}",
    f"  {BOLD}{VERMELHO}║{RESET}   {BOLD}{AMARELO}★{RESET} {BOLD}{BRANCO}F E L I Z{RESET} {BOLD}{AMARELO}★{RESET}   {BOLD}{VERMELHO}║{RESET}",
    f"  {BOLD}{VERMELHO}║                   ║{RESET}",
    f"  {BOLD}{VERMELHO}║{RESET}     {BOLD}{VERDE}N A T A L{RESET}     {BOLD}{VERMELHO}║{RESET}",
    f"  {BOLD}{VERMELHO}║                   ║{RESET}",
    f"  {BOLD}{VERMELHO}║{RESET}   {BOLD}{DOURADO}🎁  2025  🎁{RESET}   {BOLD}{VERMELHO}║{RESET}",
    f"  {BOLD}{VERMELHO}║                   ║{RESET}",
    f"  {BOLD}{VERMELHO}╚═══════════════════╝{RESET}",
    "",
    f"  {CIANO}❄  ❄  ❄  ❄  ❄  ❄{RESET}",
    "",
    f"  {BRANCO}  Que a magia do{RESET}",
    f"  {BRANCO}  Natal ilumine{RESET}",
    f"  {BRANCO}   seu caminho!{RESET}",
    "",
    f"  {CIANO}❄  ❄  ❄  ❄  ❄  ❄{RESET}",
    "",
    "",
]

def colorir_arvore(frame):
    """Colore a árvore com enfeites piscantes"""
    arvore_colorida = []
    
    for i, linha in enumerate(ARVORE):
        nova_linha = ""
        for j, char in enumerate(linha):
            if char == "★":
                # Estrela no topo pisca entre amarelo e dourado
                if frame % 2 == 0:
                    nova_linha += f"{BOLD}{AMARELO}★{RESET}"
                else:
                    nova_linha += f"{BOLD}{DOURADO}✦{RESET}"
            elif char == "█":
                # Folhagem com enfeites aleatórios
                if random.random() < 0.15:
                    cor, simbolo = random.choice(LUZES if frame % 2 == 0 else ENFEITES)
                    nova_linha += f"{cor}{simbolo}{RESET}"
                else:
                    if random.random() < 0.5:
                        nova_linha += f"{VERDE}█{RESET}"
                    else:
                        nova_linha += f"{VERDE_ESCURO}█{RESET}"
            elif char == "/":
                nova_linha += f"{VERDE}/{RESET}"
            elif char == "\\":
                nova_linha += f"{VERDE}\\{RESET}"
            elif char == "▀":
                nova_linha += f"{DOURADO}▀{RESET}"
            else:
                nova_linha += char
        arvore_colorida.append(nova_linha)
    
    return arvore_colorida

def criar_neve():
    """Cria flocos de neve caindo"""
    flocos = ["❄", "❅", "❆", "✻", "✼", "❉"]
    linha = ""
    for _ in range(60):
        if random.random() < 0.05:
            linha += f"{BRANCO}{random.choice(flocos)}{RESET}"
        else:
            linha += " "
    return linha

def montar_frame(frame):
    """Monta o frame completo com árvore, mensagem e neve"""
    arvore = colorir_arvore(frame)
    linhas = []
    
    # Neve no topo
    linhas.append(criar_neve())
    linhas.append(criar_neve())
    
    # Título
    titulo = f"    {BOLD}{AMARELO}✧･ﾟ: *✧･ﾟ:*{RESET}  {BOLD}{VERDE}FELIZ NATAL{RESET}  {BOLD}{AMARELO}*:･ﾟ✧*:･ﾟ✧{RESET}"
    linhas.append(titulo)
    linhas.append("")
    
    # Combina árvore com mensagem lateral
    max_linhas = max(len(arvore), len(FELIZ_NATAL))
    
    for i in range(max_linhas):
        linha_arvore = arvore[i] if i < len(arvore) else " " * 20
        linha_msg = FELIZ_NATAL[i] if i < len(FELIZ_NATAL) else ""
        linhas.append(f"    {linha_arvore}    {linha_msg}")
    
    # Neve embaixo
    linhas.append("")
    linhas.append(criar_neve())
    linhas.append(criar_neve())
    
    # Rodapé
    rodape = f"    {CIANO}{'═' * 50}{RESET}"
    linhas.append(rodape)
    linhas.append(f"    {BRANCO}    Pressione Ctrl+C para sair    {RESET}")
    
    return "\n".join(linhas)

def main():
    """Função principal - executa a animação"""
    try:
        esconder_cursor()
        frame = 0
        
        while True:
            limpar_tela()
            print(montar_frame(frame))
            frame += 1
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        limpar_tela()
        print(f"\n{VERDE}🎄 Feliz Natal e um Próspero Ano Novo! 🎄{RESET}\n")
    finally:
        mostrar_cursor()

if __name__ == "__main__":
    main()

