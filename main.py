from Utils.Toolkit import TestGen, Tester

filePath = "./data/data_train.csv"
targetFile = "./data/alg_sample_submission.csv"

testGen = TestGen(filePath, targetFile)
tester = Tester(testGen, kind="user_cf")

tester.evaluateTopKs([10, 20], def_shrink=20, boost=True)
