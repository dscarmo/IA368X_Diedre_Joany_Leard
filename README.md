# IA368X_Diedre_Joany_Leard

# Survival Prediction of Patients with Brain Tumor
# Predição de Sobrevivência em Pacientes com Tumor Cerebral

## Descrição Resumida do Projeto
O desafio Brain Tumor Segmentation Challenge (BraTS) contribui diretamente na provisão de dados públicos de ressonância magnética para pesquisa sobre tumor cerebrais, com diversas tarefas envolta da tarefa principal de segmentação dos tumores. Uma destas tarefas é a utilização de segmentações para estudar a possibilidade de predição de sobrevivência dos pacientes. O diagnóstico de Tumor Cerebral frequentemente acompanha uma previsão de tempo de vida do paciente, onde a acurácia desta previsão pelo médico pode melhorar a qualidade de vida antes do óbito, também chamada de qualidade de morte. Este trabalho pretende experimentar com os dados públicos do BraTS, com objetivo de prever com menor erro possível o tempo de sobrevivência dos pacientes, utilizando-se das segmentações manuais providas. Comparamos modelos de aprendizado de máquina tradicionais e baseados em Aprendizado Profundo. Os dados incluem anotações da idade e do tempo que o paciente sobreviveu, que são usados como referência. Os melhores resultados encontrados foram de ?.

## Abstract in English
The Brain Tumor Segmentation Challenge (BraTS) challenge directly contributes to the provision of public MRI data for brain tumor research, with several tasks surrounding the main task of tumor segmentation. One of these tasks is the use of segmentations to study the possibility of predicting patient survival. The diagnosis of Cerebral Tumor often accompanies a prediction of the patient's lifetime, where the accuracy of this prediction by the physician can improve the quality of life before death, also called quality of death. This work intends to experiment with the public data of BraTS, in order to predict the survival time of patients with the least possible error, using the manual segmentations provided. We compare traditional machine learning models based on Deep Learning. The data includes notes on patient's age survival in days, which is used as a reference. The best results found were from ?.

## Equipe
Diedre Santos do Carmo - 211492\
Joany - ``\
Leard de Oliveira Fernandes - 98413

## Vídeo do Projeto
[Vídeo Proposta Inicial](https://drive.google.com/file/d/1-9-7oIXs2XLczSTYfaEmQVObxV8At7mw/view?usp=sharing)

## Introdução e Motivação
Os tumores têm uma forma muito heterogênea, com diferentes graus e classificações associados. Devido a essa variação, o processamento automático de tumores cerebrais ainda é um desafio, seja para classificação, segmentação ou a tarefa específica deste trabalho, predição de sobrevivência.

O Brain Tumor Segmentation Challenge (BraTS)(citação) é um desafio anual que provê dados públicos multimodalidade (FLAIR, T1, T1 com contraste e T2) com anotações manuais de segmentação dos Glioma, um tipo de tumor cerebral. Também estão presentes tabelas de dias de sobrevivência dos pacientes dos quais as imagens foram adquiridas. A tarefa principal do BraTS é a de segmentação de tumores, usando segmentações manuais como referências. Outra das tarefas propostas pelo desafio envolve utilizar-se das segmentações para prever o tempo de sobrevivência do paciente.

A proposta deste projeto é avaliar a performance de métodos de aprendizado de máquina sobre a tarefa de predições de sobrevivência, utilizando-se como entrada tanto das imagens de MRI como de anotações manuais do tumor, além da idade do paciente. Com consciência de que estes métodos não substituiriam o profissional da saúde, mas podem servir de um auxílio na decisão média, exploramos dois caminhos metodológicos: aprendizado de maquina tradicional com baseando-se em *features* como LBP, HOG e volume do tumor, e aprendizado profundo utilizando redes neurais convolucionais (CNN) 3D, com mecanismos de atenção.

## Perguntas de Pesquisa
É possível predizer automaticamente o tempo de sobrevivência de um paciente com Glioma com métodos de aprendizado de máquina? Qual a diferença de performance entre aprendizado de máquina tradicional e profundo?

## Objetivos do projeto
Utilizar aprendizado de máquina tradicional e aprendizado de máquina profundo na tentativa de predizer tempo de sobrevivência de pacientes com Glioma a partir dos dados de ressonância magnética e anotações manuais de tumores do BraTS 2020.

![data](./assets/input.png)
*Visualização dos dados do BraTS de um sujeito. Estes dados serão entradas aos métodos propostos. As quatro modalidades são apresentadas, em ordem: FLAIR, T1, T1 com Contraste e T2. Também são exibidas na linha de baixo anotações manuais, em ordem: fundo, edema (DE), non-enhancing tumor (NET) e enhancing tumor (ET)*

## Recursos e Materiais

BraTS 2020: https://www.med.upenn.edu/cbica/brats2020/ \
**Diedre: Expandir essa seção**

## Ferramentas
| Ferramenta	| URL| 	Descrição|
| --- | --- | --- |
| Python 3| 	https://www.python.org/|	Linguagem de programação principal do projeto.|
| Scikit-Learn | https://scikit-learn.org/stable/index.html | Conjunto de ferramentas Python para aplicações em machine-learning |
| Numpy |  |  |
| Pandas |  |  |
| Orange |  |  |
|Google Colab|	https://colab.research.google.com|	Plataforma online para execução de notebooks estilo Jupyter.|

**Incluir bibliotecas aqui também?**

## Metodologia
**Aqui descrevemos metodologia como se fosse um paper.**\
**Features clássicas, extração e uso em SVM - Leard**\
**CNN, regressão de sobrevivência, atenção -Diedre**



(LEARD INICIO)

Para realização do processo de classificação de sobrevivência do sujeito, foi utilizado além da idade os dados de imagem tumoral a partir de uma base dados de 236 sujeitos. Para avaliação, validação e teste o conjunto disponibilizado foi dividido em 169 sujeitos para treino, 21 sujeitos para validação e 46 sujeitos para teste. As bases de treino e validação foram utilizadas para seleção dos melhores parâmetros e modelos utilizados no processo de classificação das imagens. As imagens disponibilizadas foram processadas no Colab utilizando a linguagem Python e o conjunto de bibliotecas Scikit-Learn, Numpy e Pandas para extração dos características da imagem. Além disso, foi utilizado o Orange para realizar a visualização das características obtidas. 

Para isso foram consideradas as seguintes características: volume do tumor, média do histograma de vetores orientados (HOG), média do histograma do padrão binário local (LBP), 10 bins do histograma HOG, e 10 bins do histograma LBP. Para todas as características de imagem, foram analisados o corpo sólido do tumor e o corpo necrosado do tumor (menor em volume), além disso foram considerados os 4 tipos de imagens disponibilizadas (T1, T1Gd, T2 e T2-FLAIR). Assim, foi possível totalizar 162 características da imagem para composição da classificação, no quais foram gravados em arquivos CSV para treino, validação e teste, conforme tabela abaixo.



| Conjunto de dados | Pixels por célula (HOG) | Raio (LBP) | Número de Pontos (LBP) | Tempo    |
| :---------------: | :---------------------: | :--------: | :--------------------: | -------- |
|         0         |          (8,8)          |     3      |           8            | 02:00:00 |
|         1         |          (8,8)          |     3      |           9            | 02:10:00 |
|         2         |          (4,4)          |     3      |           12           | 04:30:00 |



Para aplicação dos modelos de classificação os dados obtidos foram normalizados (média em zero, e desvio padrão 1). Foram considerados os seguintes modelos: *Support Vector Machine*, *Passive Agressive Classifier*, *Random Forest* e *Logistic Regression*. Para todos os modelos utilizados foi empregada a técnica de *grid-search* para obtenção dos melhores parâmetros com os dados de treino e validação. Todos os modelos obtidos foram avaliados sobre os dados de teste ao final, sem qualquer modificação de seus parâmetros, onde foram analisados precisão, revocação (*recall*), f1-score e acurácia.



apenas um teste

![](./assets/input.png)

(LEARD FIM)

<Abordagem/metodologia adotada, incluindo especificação de quais técnicas foram exploradas, tais como: aprendizagem de máquina, análise de redes, análise estatística, ou integração de uma ou mais técnicas.>

## Detalhamento do Projeto
**Vamos colocar link pra notebooks aqui, com uma breve descrição**

**Notebook ML tradicional - Leard**\
**Notebook CNN - Diedre**

<Apresente aqui detalhes da análise. Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.

Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.>
df = pd.read_excel("/content/drive/My Drive/Colab Notebooks/dataset.xlsx");
sns.set(color_codes=True);
sns.distplot(df.Hemoglobin);
plt.show();

## Evolução do Projeto
Destacar progresso seguindo o que foi escrito nas atas de reunião.

<Relate a evolução do projeto: possíveis problemas enfrentados e possíveis mudanças de trajetória. Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.>

## Resultados e Discussão
<Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

A discussão dos resultados também pode ser feita aqui na medida em que os resultados são apresentados ou em seção independente. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?>

## Conclusões
<Apresente aqui as conclusões finais do trabalho e as lições aprendidas.>
