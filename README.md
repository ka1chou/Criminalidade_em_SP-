
<p align="center">
  <img src="https://raw.githubusercontent.com/ka1chou/sigmoidal_data_science/master/Screen%20Shot%202020-06-23%20at%2011.23.58.png" >
</p>


# Criminalidade_em_SP-
**Utilizando apenas Python e um dataset, apresentamos uma pagina com dados sobre a criminalidade em São Paulo, gerada no servidor local.**

<p>   Este pequeno projeto é uma amostra do que pode ser feito utilizando a biblioteca streamlit do Python. Sem a necessidade de nenhum 
código em HTML ou CSS criamos uma apresentação que funciona direto no navegador, com servidor local, tamanha é a praticidade desta 
ferramenta. </p>

<p>

  Mesmo com poucas linhas de código já é possível formar o seguinte painel no navegador com o dataset lido: </br>
  
</p>



<p align="center">
  <img src="https://user-images.githubusercontent.com/45701541/86264020-5bee7a00-bb98-11ea-8209-139175a1a88d.png">
 </p>


A imagem abaixo mostra um mapa em 3D que representa através de pilares os índices de crimilidade, sendo que 
quanto maior o pilar, maior é o numero de ocorrências naquela região de São Paulo. Esse código é gerado em 
Python utilizando a biblioteca pydeck. Assim, de forma simples e rápida podemos construir esse nível 
de apresentações com os nossos conjuntos de dados:

<p align="center">
  <img src="https://user-images.githubusercontent.com/45701541/86264077-71fc3a80-bb98-11ea-80aa-71a09ee98c8d.png">
 </p>



<p> 
  Para iniciar a visualização é necessário digitar no terminal local o seguinte comando: </br>
  
  ```
  streamlit run [nome_do_arquivo].py
  
  ```
  
</p>
  

<p> A biblioteca streamlit é open source e gratuita, e foi feita para a construção de aplicações de dados de forma interativa 
e fácil: "Streamlit. The fastest way to build data apps"

 * streamlit [www.streamlit.io](https://www.streamlit.io)

</p>

