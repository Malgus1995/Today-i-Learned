<h2>Overview</h2>

<h3>네트워크 5계층</h3>
<ul>
	<li>1. 물리계층 : 호스트를 전송 매체와 연결하기 위한 인터페이스 규칙과 전송 매체의 특성을 다룸(대충 물리적으로 연결된 선을 가리크는 말임)</li>
	<li>2. 데이터 링크 계층 : 전기신호를 데이터로 바꾸고 전기신호의 오류를 감지하는 기능을 추가함 오류 발생시 재잔송의 방법으로 처리함</li>
	<li>3. 네트워크 계층 : 송신 호스트가 전송한 데이터가 수신 호스트까지 도착하려면 여러 중개 시스템을 거치는데, 여기서 데이터가 잘 갈수 있도록 지원하는 층이 네트워크 계층이다. 너무많은 트래픽으로 혼잡이 발생할 수있는데, 이역시 전소 경로와 관련이 있으므로, 네트워크 계층이 관리함</li>
	<li>4. 전송 계층 : 송신 프로세스와 수신의 연결 기능을 제공하고, 프로세스 사이의 안전한 데이터 전송을 지원한다. </li>
	<li>-------------------------------</li>
	<li>5. 응용 계층 : 사용자의 다양한 네트워크 응용 환경을 지원함.</li>
</ul>

<p><strong>Protocol(프로토콜)</strong> :  단말기 사이에서 데이터 통신을 원활하게 하기 위해 필요한 통신 규약</p>


<h3>네트워크 구조</h3>
<ul>
	<li>엣지(edge) : application and host(단말기)</li>
	<li>액세스 네트워크 :  유/무선 네트워크 링크</li>
	<li>네트워크 코어 : 라우터와 네트워크 속의 네트워크</li>
</ul>

<h3>엣지(edge)</h3>
<p>communication link와 packet switch의 네트워크로 연결된다. 

이들 링크는 physical media(동축케이블, 구리선, 광케이블, 라디오 스펙트럼...)로 구성된다.

이때 각각의 링크들은 다양한 전송률(transmission rate: 링크 대역폭)을 이용하여 데이터를 전송하며,

전송률은 초당 비트 수를 의미하는 bps단위를 사용한다.

한 종단 시스템이 다른 종단 시스템으로 보낼 데이터를 가지고 있을 떄,

송신 종단 시스템은 그 데이터를 세그먼트(segment)로 나누고, 각 세그먼트에 헤더(header)를 붙인다. 

이렇게 만들어진 정보 패키지는 컴퓨터 네트워크에서 패킷(packet)이라고 부른다.

패킷들은 목적지 종단 시스템으로 네트워크를 통해 보내지고, 목적지에서 원래의 데이터로 다시 조립된다.


종단 시스템(host)은 communication link와 packet switch의 네트워크로 연결된다

패킷 교환기(스위치)는 입력 통신 링크의 하나로 도착하는 패킷을 받아서 출력 통신 링크의 하나로 그 패킷을 전달한다. 패킷 스위치는 많은 형태와 특징이 있는데, 오늘날의 인터넷에서 가장 널리 사용되는 두 가지 종류로는 

라우터(router)와 링크 계층 스위치(link-layer switch)가 있다.

두 형태의 스위치는 최종 목적지 방향으로 패킷을 전달한다.



전송된 정보가 출발지(송신 종단 시스템)로부터 여러 통신 링크와 라우터들을 거쳐 목적지(수신 종단 시스템)에 이르는 길을 네트워크에서는 라우트(route) 또는 경로(path)라고 한다.



종단 시스템은 ISP(Internet Service Provider)를 통해서 인터넷에 접속한다.

각 ISP는 패킷 스위치들과 통신 링크들로 이루어진 네트워크이다.

ISP들은 종단시스템에게 56kbps 다이얼업 모뎀 접속, 케이블 모뎀이나 DSL 같은 가정용 초고속 접속, 고속 LAN 접속, 그리고 무선 접속을 포함하는 다양한 네트워크 접속을 제공한다.

*ISP: 인터넷 서비스 제공자
</p>


<h2>네트워크 엣지</h2>

<h3>클라이어이언트/서버 모델</h3>
<p>클라이언트 서버 모델(client–server model)은 서비스 요청자인 클라이언트와 서비스 자원의 제공자인 서버 간에 작업을 분리해주는 분산 애플리케이션 구조이자[1] 네트워크 아키텍처를 나타낸다. 웹 시스템도 확장된 '클라이언트 서버 시스템'으로 분류되나, 일반적으로는 클라이언트 서버 시스템이라고 하면 웹 시스템이 나오기 이전의, 사용자 PC에는 클라이언트가 설치되어 화면을 처리하고 서버에서는 자료를 처리하는 시스템을 일컫는다. 

클라이언트(영어: client 고객[*])는 서비스를 사용하는 사용자 혹은 사용자의 단말기를 가리키는 말이다.

서버(Server)란 서비스를 제공하는 컴퓨터이며, 다수의 클라이언트를 위해 존재하기 때문에 일반적으로 매우 큰 용량과 성능을 가지고 있었다. 그러나 웹 2.0에서는 클라이언트이자 동시에 서버인 환경이 많아지면서 변화가 일고 있다.

클라이언트-서버 구조로 된 네트워크 프로그램을 작성하거나, 특정 시스템이 클라이언트-서버 구조로 만들어져 있다는 것은 클라이언트와 서버가 각자의 역할에 맞게 구성됨을 말한다. 대표적인 예로는 월드 와이드 웹이 있다. 웹사이트에서는 웹 서버(IIS, Apache)가 서버 역할을 하고, 사용자가 쓰는 웹 브라우저(파이어폭스 또는 MS의 인터넷 익스플로러)가 클라이언트 프로그램이 된다. 그러나, 근래는 네트워크 응용 프로그램들의 기능이 고도화 되어 클라이언트이면서 동시에 서버이거나, 그 역인 예도 종종 볼 수 있다.
</p>


<h3>피어-피어 모델</h3>
<p>
P2P(peer-to-peer network) 혹은 동등 계층간 통신망(同等階層間通信網)은 비교적 소수의 서버에 집중하기보다는 망구성에 참여하는 기계들의 계산과 대역폭 성능에 의존하여 구성되는 통신망이다. 

P2P 통신망은 일반적으로 노드들을 규모가 큰 애드혹으로 서로 연결하는 경우 이용된다. 

*애드혹: 독립 단말끼리 외부의 도움없이 자기들 만으로 자율적인 임시적 망을 구성함을 뜻함

이런 통신망은 여러 가지로 쓸모가 있는데, 오디오나 비디오, 데이터 등 임의의 디지털 형식 파일의 공유는 매우 보편적이다. 또한, 인터넷 전화(VoIP)같은 실시간 데이터 등도 P2P 기술을 통해 서로 전달될 수 있다.

순수 P2P 파일 전송 네트워크는 클라이언트나 서버란 개념 없이, 오로지 동등한 계층 노드들(peer nodes)이 서로 클라이언트와 서버 역할을 동시에 네트워크 위에서 하게 된다.

 이 네트워크 구성 모델은 보통 중앙 서버를 통하는 통신 형태의 클라이언트-서버 모델과는 구별된다. 

 FTP 서버야 말로 P2P 파일 전송 형식이 아닌, 대표적 반례로 꼽을 수 있다. 어떤 사용자가 FTP 서버에 어떤 파일을 올리면 다른 사용자들이 내려 받는데, 올리는 쪽과 내려받는 쪽 모두 동시에 접속하지 않아도 된다.

P2P 네트워크 구조는 최근에 인터넷 상에서 멀티미디어 파일을 공유하는 용도로 많이 부각되긴 했지만, 1969년 4월 7일에 제정된 RFC(Request for Comments)란 인터넷 규약의 초기 버전부터 핵심적인 기술로 내제되어 있어 유래가 깊다.

최근의 P2P 서비스는 순수 파일 전송 네트워크에서 발달하여 그리드 컴퓨팅 기술로 진화해 웹하드 형태로 서비스되고 있다. 외부적으로 웹하드 형식으로 보이지만 실제로는 각 유저들의 저장장치에 화일이 직접 전송되어 순수 초기 P2P 네트워크와 마찬가지로 유저들의 시스템에 부하를 유발하는 공통점이 있다. 이런 웹하드 형태의 그리드 컴퓨팅 P2P 서비스로는 피디박스, 화일아이, 아이팝 등이 있다
</p>


<h3>네트워크 코어</h3>
<p>라우터들이 상호연결된 그물망 형태</p>
<p>데이터 전송 담당</p>
<ul>
	<li>circuit switching(회선 교환) : </li>
	<li>packet switching(패킷 교환) : </li>
</ul>

<h3>회선 교환</h3>
<ul>
	<li>FDM : 주파수 분할</li>
	<li>TDM : 시분할</li>
</ul>
<p>
회선 교환망은 발신자와 수신자 간에 독립적이며 동시에 폐쇄적인 통신 연결로 구성되어 있다. 이러한 1대 1 연결을 회선(circuit) 또는 채널(channel)이라고 말한다.

장점: 일단 설정된 통신은 안정적이다. 다른 요인에 의해 통신이 방해 받지 않는다.
단점
	통신 연결이 늘 보장되지는 못한다.
	네트워크 자원(network resource)을 많이 소모한다.

발신자와 수신자 또는 통신 쌍방이 통신을 시작하기 전에 미리 전용 연결(회선 또는 채널)을 설정해야만 하는 네트워크를 말한다. 통신하는 동안에는 해당 연결이 독점적으로 발신자 및 수신자에 의해서만 사용된다. 통신이 끝났을 때는 반드시 연결을 해제하는 절차가 필요하다.

초기 전화 시스템이 대표적인 예이다. 전화 가입자는 전화 통화를 위해 교환수에게 이야기하고 싶은 상대방 정보를 말하고, 교환수는 통신 연결을 위한 작업을 수행한 후에야 비로소 전화 가입자 간의 통신이 이루어진다. 이 때, 교환수가 하는 작업은 물리적으로 전화선을 쌍방간에 연결하여 설정하는 작업이다. 이 때, 해당 연결 설정이 해제되지 않는 이상 다른 사람이 현재 통화중인 사람과 통화할 수는 없다. 설사 통화중인 사람이 서로 아무런 이야기를 주고 받지 않더라도 마찬가지이다.

그 후에 다중 통신 연결을 다중화하는 것이 가능해졌다. 하지만, 다중화된 링크 속의 각각의 채널은 같은 시간에 하나의 통신에만 사용된다.

이러한 회선 교환 방식은 (일시적이든 아니든) 실제 사용하지 않더라도 연결이 설정되면, 해당 연결에 소모되는 망자원, 정확하게는 중계노드들의 대역폭을 낭비하게 되므로 비효율적이다.
</p>

<h3>패킷 교환</h3>

<p>
패킷 교환(Packet switching)은 컴퓨터 네트워크와 통신의 방식 중 하나로 현재 가장 많은 사람들이 사용하는 통신 방식이다. 작은 블록의 패킷으로 데이터를 전송하며 데이터를 전송하는 동안만 네트워크 자원을 사용하도록 하는 방법을 말한다. 

정보 전달의 단위인 패킷은 여러 통신 지점(Node)을 연결하는 데이터 연결 상의 모든 노드들 사이에 개별적으로 경로가 제어된다. 이 방식은 통신 기간 동안 독점적인 사용을 위해 두 통신 노드 사이를 연결하는 회선 교환 방식과는 달리 짤막한 데이터 트래픽에 적합하다.

장점
	네트워크 자원을 패킷 단위로 나누어 시간을 공유하므로 회선 효율성이 높다.
	트래픽이 많으면 회선 교환망은 네트워크 부하가 감소할 때까지 요청을 차단하나, 패킷 교환망은 Store-and-Forward 방식을 사용하기 때문에 데이터가 들어오는 속도와 나가는 속도를 맞출 필요 없이 각 스테이션에 맞도록 속도를 조절할 수 있다. 이로써 전송 지연이 줄어들고 통신 안정성이 늘어난다.
</p>

<h3>지연</h3>
<p>
처리지연 (Processing Delay)
처리지연은 각 노드로 들어온 패킷의 IP 헤더를 확인하여 어느 목적지로 보낼지 결정하는 시간이다. 이러한 목적지 결정 이외에도 각 패킷의 오류를 검사하는 시간도 처리지연에 포함된다.


큐잉지연(Queuing Delay)
큐잉지연은 저장 후 전송과정에서 각 노드에 먼저 들어온 패킷이 처리 완료될 때까지 일시적으로 대기하는 지연을 의미한다. 
만약 큐가 비어있다면 큐잉지연은 0 이지만 많은 패킷이 큐에 대기 하고 있다면 큐잉지연이 크다. 또한 큐의 크기는 고정되어 있기 때문에 만약 일시적으로 큐의 범위를 벗어나는 많은 패킷이 라우터로 들어오게 되면 큐의 범위를 초과하여 초과한 패킷들의 손실(packet loss)이 발생할 수도 있다.


전송지연(Transmission Delay or Store-and-Forward Delay)
전송지연은 전달하고자 하는 패킷의 모든 비트를 전송하기 위해서 모든 비트들을 링크로 밀어내는 시간을 의미한다. 예를 들어 패킷의 길이가 L 비트이고 전송률이 R bps인 경우 L/R이 전송지연이 된다. 만약 패킷의 길이보다 전송률이 더 높다면 전송지연은 발생하지 않을 것이다.


전파지연(Propagation Delay)
전파지연은 물리적인 통신선로를 통하여 전기적인 신호가 송신자로부터 수신자까지 도달하는 시간을 의미한다. 대충말해 거리라는 소리다.
 따라서 전파지연은 통신선의 종류에 따라 크게 달라진다. 만약, 320 Kbit의 데이터를 32 Kbps 전송률(대역폭)을 가진 선로를 통해 전달한다고 하면,

 쉽게 생각하기에 10 초가 걸린다고 생각할 수 있다. 

 하지만 이것은 회선이 이용할 수 있는 대역만을 가지고 계산한 것이므로 전파지연이 생략된 값이다. 

 따라서 정확한 시간을 원한다면 송신자로부터 수신자까지 전기적인 신호가 도달하는 전파지연도 함께 고려되어야 한다.

만약 100 Mbps의 대역폭을 같은 선로를 이용하여 데이터를 주고 받는다면 일반적으로 처리지연, 전송지연, 전파지연은 일정한 값을 가진다. 하지만 송신지와 목적지가 같음에도 불구하고 큐잉지연은 매번 달라질 수 있다. 이는 네트워크 상황은 수시로 변할 수 있기 때문이다.	
</p>
<h4>패킷 지연시간 = 전송 + 전파 + 큐잉 + 처리</h4>
