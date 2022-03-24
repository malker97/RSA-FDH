##### 生成密钥

```bash
openssl genrsa -out private.pem 1024
```

##### 用密钥生成公钥

```bash
openssl rsa -in private.pem -pubout -out public.pem
```



##### 加密指令

```bash
openssl rsautl -encrypt -in plaintext.txt  -inkey public.pem  -pubin -out ciphertext.txt
```

##### 解密指令

```bash
openssl rsautl -decrypt -in ciphertext.txt  -inkey private.pem -out decCryMsg.txt
```

#### 签名部分

##### RSA签名算法

$\delta = m^d \ mod \ n$

##### RSA-FDH签名算法为

$\delta = H(m)^d \ mod \ n$

##### RSA验证签名算法

$m=\delta^e \ mod \ n$

##### RSA-FDH验证签名算法

$H(m) = \delta^e mod \ n $

#### 模拟场景

##### 场景一

**第一个场景**：战场上，Bob要给Alice传递一条消息，内容为某一指令。

RSA的加密过程如下：

（1）Alice生成一对密钥（公钥和私钥），私钥不公开，Alice自己保留。公钥为公开的，任何人可以获取。

（2）Alice传递自己的公钥给Bob，Bob用Alice的公钥对消息进行加密。

（3）Alice接收到Bob加密的消息，利用Alice自己的私钥对消息进行解密。

总的来说就是Bob用了Alice给的**公钥**加密了消息，然后发给了Alice

##### 场景二

**第二个场景：**Alice收到Bob发的消息后，需要进行回复“收到”。

RSA签名的过程如下：

（1）Alice生成一对密钥（公钥和私钥），私钥不公开，Alice自己保留。公钥为公开的，任何人可以获取。

（2）Alice用自己的私钥对消息加签，形成签名，并将加签的消息和消息本身一起传递给Bob。

（3）Bob收到消息后，在获取Alice的公钥进行验签，如果验签出来的内容与消息本身一致，证明消息是A回复的。

总的来说就是Alice收到Bob的消息以后，对消息用**私钥**进行加签名，然后发送回鲍勃，Bob验证签名来确定是不是Alice的回复