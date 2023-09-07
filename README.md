# News Text Classification Demo / 新闻文本分类简单项目示例

本项目是一个简单的新闻文本分类任务，部分代码已经被提交至合肥工业大学数据挖掘 (数据与智能工程，0521550X）课程作业。本代码仅供参考，不建议用作作业提交。

This is a demo project for news text classification, part of this work has been admitted for the homework of Hefei University of Technology Data Mining course(0521550X). **I strongly do not recommend you submit this project for homework again.**

本项目不包含数据集！

This project does not contain any dataset!

Please Star!

![version](https://img.shields.io/badge/NTC-v0.1-blue)
[![Page Views Count](https://badges.toozhao.com/badges/01H9QMHGR2J0E0YE6YEGQQKYE3/green.svg)](https://badges.toozhao.com/stats/01H9QMHGR2J0E0YE6YEGQQKYE3 "Get your own page views count badge on badges.toozhao.com")


## Contents

- [Background](#background)
- [Usage](#Usage)
- [Maintainers](#maintainers)
- [License](#license)

## Background
[新闻文本分类](!https://huggingface.co/tasks/text-classification)是自然语言处理领域的经典任务，本项目通过一些经典机器学习方法处理了一个公开新闻语料库。

[Text classification](!https://huggingface.co/tasks/text-classification) is a fundamental task in the Natural Language Processing (NLP) field. For this project, we select a public News corpus and use some classic, machine learning methods to process it.

## Usage

### 数据预处理 / Data preprocessing
本项目针对的数据集是JSON格式，一条数据包含标题-内容-其他信息等多个数据。因此需要对数据集进行预处理，转换JSON格式，提取文本内容，提取标题，打标签等。这些代码均在 `data_preprocessing` 中。

We processing the JSON format dataset, a single data containing Header-Content-Others information. It is necessary to process the dataset and transform it to the proper format before feeding it to the model.

All these preprocessing codes are in the `data_preprocessing`.

### 算法 / algorithm
使用一些经典机器学习算法对处理后的文本进行分类，这里包含了多种经典机器学习方法。包含在 `algorithm` 中。

All the algorithms tested in this demo project are in the `algorithm`.

## Maintainers

[@Sensente](https://github.com/Sensente).

## License

[Apache2.0](LICENSE) © Sensente
