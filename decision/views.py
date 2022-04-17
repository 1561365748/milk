from django.shortcuts import render
from django.http import HttpResponseRedirect
# 导入csv格式文件
import csv
from pathlib import Path
import subprocess
# 导入 DictVectorizer 模块，以便将数据转化为0或1的符号
from sklearn.feature_extraction import DictVectorizer

# 导入 precessing,tree 模块
from sklearn import preprocessing, tree

# 导入 accuracy_score 模块，用以计算该模型准确率
from sklearn.metrics import accuracy_score

# from sklearn.metrics import recall_score

# 将三个品牌的数据集进行特征化处理之后，分别打开csv文件，进行读取
from sklearn.tree import plot_tree
mytext=" "
prediction=""
def check_valid_path(path):
    """检查文件路径是否有效，并返回以'/'分割的文件路径"""
    if '\\' in path:
        elements = str(Path(path)).split(sep='\\')
        final_path = Path('/'.join(elements))
    elif '/' in path:
        final_path = Path(path)
    else:
        if not Path(path).exists():
            raise Exception("Error: File path pattern is not correct.")
        else:
            final_path = Path(path)
    if not final_path.exists():
        raise Exception("Error: Your file path does not exist.")
    if final_path != '':
        return final_path
    else:
        return None
def dot2png(dot_file_path=None, img_path=None):
    """决策树可视化中.dot文件转化为.png图片的函数"""
    if not dot_file_path:
        raise Exception(".dot file is not given.")
    elif not dot_file_path.endswith('.dot'):
        raise Exception("file provided is not '.dot' type.")

    DOT_PATH = check_valid_path(dot_file_path)

    if not img_path:
        img_path = 'dt_png.png'
    elif not img_path.endswith('.png'):
        raise Exception("image file not end with '.png'.")

    IMG_PATH = img_path

    cmd_args = ['dot', '-Tpng', DOT_PATH, '-o', IMG_PATH]

    cmd_pro = subprocess.Popen(args=cmd_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = cmd_pro.stdout.read().decode('gbk')
    if retval == '':
        print("successfully create file " + IMG_PATH)
    else:
        print("The program encountered some error: ")
        print(retval)
def start(request):
    if request.method == 'GET':
        return render(request, 'decision.html')

    elif request.method=='POST':
        if request.POST['ask']!='':
            mytext = request.POST['ask']
            text = eval(mytext)
            prediction=""
            clients_data = open('D:\\python\\Django-2.2.24\\milk\\tree\\1.csv', 'rt')
            reader = csv.reader(clients_data)
            headers = next(reader)

            # 提取数据集中的特征值，经过处理之后有8个特征值
            features_table = []

            # 预测得出的客户的选择，用0或1表示，1表示会买，0表示不会买
            results_table = []

            # 以下为数据的读取方式
            for row in reader:
                results_table.append(row[-1])
                features_table.append(dict(zip(headers[1:-1], row[1:-1])))
            # print(results_table)

            # 找出特征量分别为……，共有8个
            feature = DictVectorizer(sparse=False)

            # 将特征表由字典转换成稀疏矩阵来处理，便于查看
            baseX = feature.fit_transform(features_table)

            # 随后将选择结果转换成数组形式打印出来，便于下次预测
            results = preprocessing.LabelBinarizer()
            baseY = results.fit_transform(results_table)
            # print(baseY)
            # 把基于csv特征数据集的决策树创建起来
            clf = tree.DecisionTreeClassifier(criterion='entropy', random_state=0)
            clf = clf.fit(baseX, baseY)
            print("决策树:", str(clf))
            # 导出决策树为图片
            with open('D:\\python\\Django-2.2.24\\milk\\tree\\treeone.dot', 'w') as f:
                dot_data = tree.export_graphviz(clf, out_file=None)
                f.write(dot_data)

            dot2png(dot_file_path="D:\\python\\Django-2.2.24\\milk\\tree\\treeone.dot",
                    img_path="D:\\python\\Django-2.2.24\\milk\\static\img\\tree.png")


            prediction = clf.predict(text)
            print("预测结果为")
            print(str(prediction))

            print("预测准确率为:")
            accuracy=accuracy_score(baseY, clf.predict(baseX))
        return render(request,'decision.html', locals())

