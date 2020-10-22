import openpyxl
class Read_Excel:
    def get_exceldata(self):
        excel1=openpyxl.load_workbook('D:\\2020\\vscode\my-project\data.xlsx')
        sheet1=excel1['Sheet1']
        # print(sheet1.cell(row=1,column=1).value)
        # print(sheet1.max_row,sheet1.max_column)
        maxrow=sheet1.max_row
        maxcolumn=sheet1.max_column
        listdata=[]
        for x in range(2,maxrow+1):
            dict1={}
            for y in range(1,maxcolumn+1):
                #print(sheet1.cell(row=x,column=y).value)
                value=sheet1.cell(x,y).value
                dict1[sheet1.cell(1,y).value]=value
            listdata.append(dict1)
        #print(listdata)
        return (listdata)

Read_Excel().get_exceldata()