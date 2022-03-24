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

