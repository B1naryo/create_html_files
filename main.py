# Número total de arquivos a serem criados
total_arquivos = 114

# Loop para criar os arquivos
for i in range(1, total_arquivos + 1):
    nome_arquivo = f"{i}.html"
    with open(nome_arquivo, "w") as arquivo:
        # Conteúdo básico para os arquivos HTML
        conteudo = """<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu Vertical</title>
    <link rel="stylesheet" href="css/styles.css">
</head>

<body>
    <div class="container">
        <div id="menu">
            <ul>
                <li class="menu-item">
                    <a href="#">RECON</a>
                    <ul class="submenu">
                        <li><a href="1.html">Public info gathering</a></li>
                        <li><a href="2.html">Root domains</a></li>
                        <li><a href="3.html">Subdomain Enum</a></li>
                        <li><a href="4.html">Subdomain Takeover</a></li>
                        <li><a href="5.html">Webs recon</a></li>
                        <li><a href="6.html">Network Scanning</a></li>
                        <li><a href="7.html">Host Scanning</a></li>
                        <li><a href="8.html">Packet Scanning</a></li>
                    </ul>
                </li>
                <li class="menu-item">
                    <a href="#">ENUMERATION</a>
                    <ul class="submenu">
                        <li><a href="9.html">Files</a></li>
                        <li><a href="10.html">SSL/TLS</a></li>
                        <li><a href="11.html">Ports</a></li>
                        <li class="submenu-item has-submenu">
                            <!-- Adicionando a classe has-submenu para indicar que este item possui um submenu -->
                            <a href="#">Web Attacks</a>
                            <ul class="submenu">
                                <li><a href="12.html">General Info</a></li>
                                <li><a href="13.html">Quick tricks</a></li>
                                <li><a href="14.html">Headers inkections</a></li>
                                <li><a href="16.html">Bruteforcing</a></li>
                                <li><a href="16.html">Online hashes cracked</a></li>
                                <li><a href="17.html">Crawl/Fuzz</a></li>
                                <li><a href="18.html">LFI/RFI</a></li>
                                <li><a href="19.html">File upload</a></li>
                                <li><a href="20.html">SQLi</a></li>
                                <li><a href="21.html">SSRF</a></li>
                                <li><a href="22.html">Open redirects</a></li>
                                <li><a href="23.html">XSS</a></li>
                                <li><a href="24.html">CSP</a></li>
                                <li><a href="25.html">XXE</a></li>
                                <li><a href="26.html">Cookie Padding</a></li>
                                <li><a href="27.html">CORS</a></li>
                                <li><a href="28.html">CSRF</a></li>
                                <li><a href="29.html">Web Cache Poisoning</a></li>
                                <li><a href="30.html">Broken Links</a></li>
                                <li><a href="31.html">Clickjacking</a></li>
                                <li><a href="32.html">HTTP Request Smuggling</a></li>
                                <li><a href="33.html">Web Sockets</a></li>
                                <li><a href="34.html">CRLF</a></li>
                                <li><a href="35.html">IDOR</a></li>
                                <li><a href="36.html">Web Cache Deception</a></li>
                                <li><a href="37.html">Session fixation</a></li>
                                <li><a href="38.html">Email attacks</a></li>
                                <li><a href="39.html">Pastekacking</a></li>
                                <li><a href="40.html">HTTP Parameter pollution</a></li>
                                <li><a href="41.html">SSTI</a></li>
                                <li><a href="42.html">Prototype Pollution</a></li>
                                <li><a href="43.html">Command Injection</a></li>
                                <li><a href="44.html">Deserialization</a></li>
                                <li><a href="45.html">DNS rebinding</a></li>

                            </ul>
                        </li>
                        <li class="submenu-item has-submenu">
                            <a href="#">Web Technologies</a>
                            <ul class="submenu">
                                <li><a href="46.html">APIs</a></li>
                                <li><a href="47.html">JS</a></li>
                                <li><a href="48.html">ASP.NET</a></li>
                                <li><a href="49.html">JWT</a></li>
                                <li><a href="50.html">GitHub</a></li>
                                <li><a href="51.html">GitLab</a></li>
                                <li><a href="52.html">WAFs</a></li>
                                <li><a href="53.html">Firebird</a></li>
                                <li><a href="54.html">Wordpress</a></li>
                                <li><a href="55.html">Wordpress</a></li>
                                <li><a href="56.html">WebDav</a></li>
                                <li><a href="57.html">Joomla</a></li>
                                <li><a href="58.html">Jenkins</a></li>
                                <li><a href="59.html">IIS</a></li>
                                <li><a href="60.html">VHosts</a></li>
                                <li><a href="61.html">Firebase</a></li>
                                <li><a href="62.html">OWA</a></li>
                                <li><a href="63.html">OAuth</a></li>
                                <li><a href="64.html">Flask</a></li>
                                <li><a href="65.html">Symfony && Twig</a></li>
                                <li><a href="66.html">Drupal</a></li>
                                <li><a href="67.html">NoSQL(MongoDB, CouchDB)</a></li>
                                <li><a href="68.html">RoR(Ruby on Rails)</a></li>
                                <li><a href="69.html">JBoss-Java Deserialization</a></li>
                                <li><a href="70.html">OneLogin-SAM Login</a></li>
                                <li><a href="71.html">Flash SWF</a></li>
                                <li><a href="72.html">Nginx</a></li>
                                <li><a href="73.html">Python</a></li>
                                <li><a href="74.html">Tomcat</a></li>
                                <li><a href="75.html">Adobe AEM</a></li>
                                <li><a href="76.html">Magento</a></li>
                                <li><a href="77.html">SAP</a></li>
                                <li><a href="78.html">PHP</a></li>
                                <li><a href="79.html">MFA</a></li>
                                <li><a href="80.html">GWT</a></li>
                                <li><a href="81.html">Jira</a></li>
                                <li><a href="82.html">OIDC(Open ID Connect)</a></li>
                                <li><a href="83.html">ELK</a></li>
                                <li><a href="84.html">Sharepoint</a></li>
                                <li><a href="85.html">Others</a></li>

                            </ul>
                        </li>
                        <li class="submenu-item has-submenu">
                            <a href="#">Cloud</a>
                            <ul class="submenu">
                                <li><a href="86.html">General</a></li>
                                <li><a href="87.html">Cloud Info Gathering</a></li>
                                <li><a href="88.html">AWS</a></li>
                                <li><a href="89.html">Azure</a></li>
                                <li><a href="90.html">GCP</a></li>
                                <li><a href="91.html">Docker&&Kubernetes</a></li>
                                <li><a href="92.html">CDN-Comain Fronting</a></li>
                            </ul>
                        </li>
                    </ul>
                </li>


                <li class="menu-item">
                    <a href="#">EXPLOITATION</a>
                    <ul class="submenu">
                        <li><a href="93.html">Payloads</a></li>
                        <li><a href="94.html">Reverse Shells</a></li>
                        <li><a href="95.html">File transfer</a></li>
                    </ul>
                </li>
                <li class="menu-item">
                    <a href="#">POST EXPLOITATION</a>
                    <ul class="submenu">
                        <li><a href="96.html">Linux</a></li>
                        <li><a href="97.html">Pivoting</a></li>
                        <li><a href="98.html">Windows</a></li>
                    </ul>
                </li>
                <li class="menu-item">
                    <a href="#">MOBILE</a>
                    <ul class="submenu">
                        <li><a href="99.html">General</a></li>
                        <li><a href="100.html">Android</a></li>
                        <li><a href="101.html">iOS</a></li>
                    </ul>
                </li>
                <li class="menu-item">
                    <a href="#">OTHERS</a>
                    <ul class="submenu">
                        <li><a href="102.html">Burp Suite</a></li>
                        <li><a href="103.html">Password cracking</a></li>
                        <li><a href="104.html">Code review</a></li>
                        <li><a href="105.html">Pentest Web checklist</a></li>
                        <li><a href="106.html">Internal Pentest</a></li>
                        <li><a href="107.html">Web fuzzers review</a></li>
                        <li><a href="108.html">Recon suites review</a></li>
                        <li><a href="109.html">Subdomain tools review</a></li>
                        <li><a href="110.html">Random</a></li>
                        <li><a href="111.html">MAster assessment mindmaps</a></li>
                        <li><a href="112.html">BugBounty</a></li>
                        <li><a href="113.html">SExploiting</a></li>
                        <li><a href="114.html">tools everywhere</a></li>
                    </ul>
                </li>
                <!-- Adicione mais itens de menu e submenus conforme necessário -->
            </ul>
        </div>
    </div>
    <div id="conteudo">
        <div id="conteudo">
            <h1>Fases de Pentest em Web</h1>
            <p>O teste de penetração em aplicações web, conhecido como web pentest, é um processo sistemático usado para identificar e explorar vulnerabilidades em aplicações da web. Este processo inclui várias fases, tais como:</p>
            <h2>1. RECON</h2>
            <p>A fase de reconhecimento envolve a coleta de informações sobre a aplicação web, incluindo arquitetura, tecnologias utilizadas, endpoints, e possíveis pontos de entrada.</p>
            <h2>2. ENUMERATION</h2>
            <p>Na fase de enumeração, o testador identifica ativamente os recursos disponíveis na aplicação web, como páginas, formulários, APIs, parâmetros, e outras funcionalidades.</p>
            <h2>3. EXPLOITATION</h2>
            <p>Nesta fase, o testador tenta explorar as vulnerabilidades identificadas para obter acesso não autorizado à aplicação web. Isso pode envolver a exploração de falhas de segurança, como injeção de SQL, cross-site scripting (XSS), e autenticação
                defeituosa.</p>
            <h2>4. POST EXPLOITATION</h2>
            <p>Após obter acesso à aplicação web, o testador realiza atividades de pós-exploração, como escalonamento de privilégios, movimento lateral, e exfiltração de dados sensíveis.</p>
            <h2>5. MOBILE</h2>
            <p>Em testes de penetração móveis, o foco está na avaliação da segurança de aplicativos móveis e infraestrutura associada, como APIs e servidores de backend usados por aplicativos móveis.</p>
            <h2>6. Outras Fases</h2>
            <p>Além das fases mencionadas acima, um web pentest pode incluir outras etapas específicas, dependendo dos requisitos do projeto e do ambiente de teste.</p>
            <p>Esta página foi criada para facilitar o processo de entendimento e aplicação das fases de pentest em aplicações web, fornecendo uma visão geral das etapas envolvidas e dos objetivos de cada uma.</p>

        </div>



    </div>
    <script src="js/scripts.js"></script>
</body>

</html>"""
        arquivo.write(conteudo)

print(f"{total_arquivos} arquivos HTML foram criados com sucesso!")

