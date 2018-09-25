
## 目录结构：

```
.
├── Scrapy to wikidata and baidu baike      // scrapy爬虫项目路径(已爬好)
│   └── load_category
│   ├── load_page // 爬取wikipedia
│   └── baidu    // 爬取百度百科        
├── data\ processing    // 数据清洗(已无用)
│   └── data
|___ py2neo // python操作neo4j数据库
|
|————text_keyword_and_KG_dictionary // 知识图谱词典和基于词典的文本摘要
├── demo     // django项目路径
│   ├── Model  // 模型层，用于封装Item类，以及neo4j和csv的读取
│   ├── demo   // 用于写页面的逻辑(View)
│   ├── label_data    // 标注训练集页面的保存路径
│   │   └── handwork
│   ├── static    // 静态资源
│   │   ├── css
│   │   ├── js
│   │   └── open-iconic
│   ├── templates   // html页面
│   └── toolkit   // 工具库，包括预加载，命名实体识别
│   └── KNN_predict   
├── KNN_predict    // KNN算法预测标签
├── dfs_tree_crawler    

```



## 可复用资源

- entity1.csv : 已经爬好的人工智能的百科页面的结构化csv文件
- new_node.csv : 已经爬好的子节点实体
- labels.txt： 5000多个手工标注的实体类别
- predict_labels.txt:  KNN算法预测的13W多个实体的类别




## 项目配置

**系统需要安装：**

- scrapy     ---爬虫框架
- django     ---web框架
- neo4j       ---图数据库
- jieba      ---分词、词性标注
- py2neo    ---python连接neo4j的工具
- pyfasttext    ---facebook开源的词向量计算框架
- pinyin  ---获取中文首字母小工具
- 预训练好的词向量模型wiki.zh.bin（仅部署网站的话不需要下载）    ---下载链接：http://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.zh.zip
- mongoDB  ---存储文档数据
- pymongo  ---python操作mongoDB的工具
- HanLP    --- 开源NLP算法包


（以上部分除了neo4j在官网下，wiki.zh.bin在亚马逊s3下载，其它均可直接用pip3 install 安装）



**项目部署：**

1. 将entity.csv导入neo4j：开启neo4j，进入neo4j控制台。将entity1.csv放入neo4j安装目录下的/import目录。在控制台依次输入：

```
// 将hudong_pedia.csv 导入
LOAD CSV WITH HEADERS  FROM "file:///entity1.csv" AS line  
CREATE (p:HudongItem{title:line.title,image:line.image,detail:line.detail,url:line.url,openTypeList:line.openTypeList,baseInfoKeyList:line.baseInfoKeyList,baseInfoValueList:line.baseInfoValueList})  


```
// 创建索引
CREATE CONSTRAINT ON (c:title)
ASSERT c.title IS UNIQUE
```

以上两步的意思是，将entity1.csv导入neo4j作为结点，然后对title属性添加UNIQUE（唯一约束/索引）

*（如果导入的时候出现neo4j jvm内存溢出，可以在导入前，先把neo4j下的conf/neo4j.conf中的dbms.memory.heap.initial_size 和dbms.memory.heap.max_size调大点。导入完成后再把值改回去）*



进入/wikidataSpider/wikidataProcessing中，将new_node.csv,wikidata_relation.csv,wikidata_relation2.csv三个文件放入neo4j的import文件夹中（运行relationDataProcessing.py可以得到这3个文件），然后分别运行
```
// 导入新的节点
LOAD CSV WITH HEADERS FROM "file:///new_node.csv" AS line
CREATE (:NewNode { title: line.title })

//添加索引
CREATE CONSTRAINT ON (c:NewNode)
ASSERT c.title IS UNIQUE

//导入entity1和新加入节点之间的关系
LOAD CSV  WITH HEADERS FROM "file:///relations.csv" AS line
MATCH (entity1:HudongItem{title:line.title}) , (entity2:NewNode{title:line.NewNode})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)

LOAD CSV  WITH HEADERS FROM "file:///relations.csv" AS line
MATCH (entity1:HudongItem{title:line.title}) , (entity2:HudongItem{title:line.new_node})
CREATE (entity1)-[:RELATION { type: line.relation }]->(entity2)
```


//我们建索引的时候带了label，因此只有使用label时才会使用索引，这里我们的实体有两个label，所以一共做2*2=4次。当然，可以建立全局索引，即对于不同的label使用同一个索引
                                                            
          
                                                                                                                         
```





以上步骤是导入爬取到的关系



2. 下载词向量模型：http://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.zh.zip  
  将wiki.zh.bin放入 KNN_predict 目录 。 （如果只是为了运行项目，步骤2可以不做，预测结果已经离线处理好了）



3. 进入demo/Model/neo_models.py,修改第9行的neo4j账号密码，改成你自己的
4. 进入demo目录，然后运行脚本：

```
sudo sh django_server_start.sh
```

这样就成功的启动了django。我们进入8000端口主页面，输入文本，即可看到以下命名实体和分词的结果（确保django和neo4j都处于开启状态）



### 实体查询

实体查询部分，我们能够搜索出与某一实体相关的实体，以及它们之间的关系：
![image](https://raw.githubusercontent.com/CrisJk/SomePicture/master/blog_picture/entitySearch.png)

![](https://raw.githubusercontent.com/CrisJk/SomePicture/master/blog_picture/entitySearch2.png)

### 关系查询

关系查询即查询三元组关系entity1-[relation]->entity2 , 分为如下几种情况:

* 指定第一个实体entity1
* 指定第二个实体entity2
* 指定第一个实体entity1和关系relation
* 指定关系relation和第二个实体entity2
* 指定第一个实体entity1和第二个实体entity2
* 指定第一个实体entity1和第二个实体entity2以及关系relation

下图所示，是指定关系relation和第二个实体entity2的查询结果

![](https://raw.githubusercontent.com/CrisJk/SomePicture/master/blog_picture/relationSearch.png)



![](https://raw.githubusercontent.com/CrisJk/SomePicture/master/blog_picture/relationSearch2.png)




## 思路

### 图谱实体获取：

1.根据人工智能词条，按照筛法提取名词（分批进行，每2000条1批，每批维护一个不可重集合）

2.将9批词做交集，生成词典

3.将词典中的词在wiki中进行爬取，抛弃不存在的页面，提取页面内容，存到数据库中

4.根据页面内容，提取每一个词条页面的特征，构造相似度的比较方法，使用KNN进行分类

5.最后获取每个词条的所属类别，同时能够剔除无关词条





### 页面分类

#### 分类器：KNN算法

- 无需表示成向量，比较相似度即可
- K值通过网格搜索得到

#### 定义两个页面的相似度sim(p1,p2)：

- 
  title之间的词向量的余弦相似度(利用fasttext计算的词向量能够避免out of vocabulary)
- 2组openType之间的词向量的余弦相似度的平均值
- 相同的baseInfoKey的IDF值之和（因为‘中文名’这种属性贡献应该比较小）
- 相同baseInfoKey下baseInfoValue相同的个数
- 预测一个页面时，由于KNN要将该页面和训练集中所有页面进行比较，因此每次预测的复杂度是O(n)，n为训练集规模。在这个过程中，我们可以统计各个分相似度的IDF值，均值，方差，标准差，然后对4个相似度进行标准化:**(x-均值)/方差**
- 上面四个部分的相似度的加权和为最终的两个页面的相似度，权值由向量weight控制，通过10折叠交叉验证+网格搜索得到




