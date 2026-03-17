#include <iostream>
#include <vector>

int main() {
    int n;
    std::cout << "Digite um numero positivo N: ";
    
    // Validação de entrada
    while(!(std::cin >> n) || n < 1) {
        std::cout << "Entrada invalida. Digite um numero positivo N: ";
        std::cin.clear();
        std::cin.ignore(10000, '\n');
    }

    std::vector<int> primos;

    // Otimização: Tratamos o 2 separadamente se N for >= 2
    if (n >= 2) primos.push_back(2);

    // Começamos do 3 e pulamos de 2 em 2 (apenas ímpares)
    for(int i = 3; i <= n; i += 2) {
        bool isPrime = true;
        for(int j = 3; j * j <= i; j += 2) { // Também só testa divisores ímpares
            if(i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if(isPrime) primos.push_back(i);
    }

    std::cout << "\nValor de N: " << n << std::endl;
    std::cout << "Numeros primos encontrados: ";
    
    for(size_t i = 0; i < primos.size(); i++) {
        std::cout << primos[i];
        if(i < primos.size() - 1) std::cout << " - "; // Só coloca o traço se não for o último
    }

    std::cout << "\nQuantidade de numeros primos encontrados: " << primos.size() << std::endl;

    return 0; 
}