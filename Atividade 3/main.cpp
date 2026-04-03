#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <numeric>
#include <iomanip>


using namespace std; // Evita a necessidade de escrever std:: antes de cada elemento da biblioteca padrão
using namespace std::chrono; // Evita a necessidade de escrever std::chrono:: antes de cada elemento da biblioteca chrono

// algoritmo lento

void bubbleSort(vector<int>& arr) {
    int n = arr.size(); // Obtém o tamanho do vetor
    for (int i = 0; i < n - 1; i++) { // Loop externo para controlar o número de passagens
        for (int j = 0; j < n - i - 1; j++){ // Loop interno para comparar elementos adjacentes
            if (arr[j] > arr[j + 1]) { // Se o elemento atual for maior que o próximo, troca os elementos
                swap(arr[j], arr[j + 1]); // Função de troca da biblioteca padrão para trocar os elementos
            }
        }
    }
}

// função para medir e executar 5 vezes

void testarAlgoritmo(string nome, void (*func)(vector<int>&), vector<int> dados) {
    vector<double> tempos; // vetor para armazenar os tempos de execução
    cout << "Algoritmo: " <<nome << endl; // Imprime o nome do algoritmo

    for (int i = 0; i < 5; i++){ // Loop para executar o algoritmo 5 vezes
        vector<int> copia = dados; // Cria uma cópia dos dados para cada execução
        auto start = high_resolution_clock::now(); // Marca o início da execução
        func(copia); // Executa o algoritmo de ordenação
        auto end = high_resolution_clock::now(); // Marca o fim da execução
        
        duration<double> diff = end - start; // Calcula a duração da execução
        tempos.push_back(diff.count()); // Armazena o tempo de execução no vetor
        cout << "Execucao " << i + 1 << ": " << fixed << setprecision(4) << diff.count() << " s" << endl; // Imprime o tempo de execução formatado
    }

    double soma = accumulate(tempos.begin(), tempos.end(), 0.0); // Calcula a soma dos tempos de execução
    cout << "Media: " << (soma / 0.5) << "s/n" << endl; // Imprime a média dos tempos de execução
}


// Wrapper para o QuickSort da biblioteca padrão

void quickSortWrapper(vector<int>& arr) {
    sort(arr.begin(), arr.end()); // Usa a função sort da biblioteca padrão para ordenar o vetor
}

int main() {
    // 1. abrir o arquivo e ler os dados
    ifstream fin("arq.txt"); // Abre o arquivo de entrada
    if(!fin) { // Verifica se o arquivo foi aberto com sucesso
        cerr << "Erro ao abrir o arquivo!" << endl; // Imprime uma mensagem de erro
        return 1; // Encerra o programa com código de erro
    }

    // 2. ler números

    vector<int> numeros; // Vetor para armazenar os números lidos do arquivo
    int n; // Variável para armazenar cada número lido
    while(fin >> n) { // loop para ler os números do arquivo até o final
        numeros.push_back(n); // Adiciona o número lido ao vetor
    }
    fin.close(); // Fecha o arquivo de entrada

    if(numeros.empty()) { // Verifica se o vetor de números está vazio
        cerr << "Nenhum numero encontrado no arquivo!" << endl; // Imprime uma mensagem de erro
        return 1; // Encerra o programa com código de erro
    }

    //3. medição de tempos

    testarAlgoritmo("Bubble Sort", bubbleSort, numeros); // Testa o algoritmo Bubble Sort
    testarAlgoritmo("Quick Sort", quickSortWrapper, numeros); // Testa o algoritmo Quick Sort

    //4. Salvar os resultados em um arquivo de saída

    sort(numeros.begin(), numeros.end()); // Ordena os números usando a função sort da biblioteca padrão
    ofstream fout("arq-ordenado.txt"); // Abre o arquivo de saída
    for(size_t i = 0; i < numeros.size(); i++) { // Loop para escrever os números ordenados no arquivo de saída
        fout << numeros[i] << (i == numeros.size() - 1 ? "" : " "); // Escreve cada número em uma nova linha
    }
    fout.close(); // Fecha o arquivo de saída

    cout << "Resultado salvo em arq-ordenado.txt" << endl; // Imprime uma mensagem indicando que o resultado foi salvo
    return 0; // Encerra o programa com código de sucesso
}