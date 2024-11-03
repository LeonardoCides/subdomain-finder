import socket
import os

os.system('clear')
def find_subdomains(domain, wordlist_file):
    found_subdomains = []
    
    # Verifica se o arquivo existe
    if not os.path.isfile(wordlist_file):
        print(f"Erro: O arquivo {wordlist_file} não foi encontrado.")
        return found_subdomains

    with open(wordlist_file, 'r') as file:
        for line in file:
            subdomain = line.strip()
            full_domain = f"{subdomain}.{domain}"
            try:
                # Faz a consulta DNS usando socket
                socket.gethostbyname(full_domain)
                found_subdomains.append(full_domain)
                print(f"Subdomínio encontrado: \033[32m{full_domain}\033[0m")
            except socket.gaierror:
                pass  # Subdomínio não existe
    return found_subdomains

# Exemplo de uso
domain = input("domain: ")
wordlist_file = "/home/axl/Documents/wordlist.txt"  # Caminho completo do arquivo
result = find_subdomains(domain, wordlist_file)
print(f"Subdomínios encontrados para {domain}: {result}")
