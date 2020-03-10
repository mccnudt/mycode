
Public Sub 处理数据()

Dim shtname, newsht As String '定义要建立的工作表名称
Do
    shtname = InputBox("请输入要汇总的工作表名称")
Loop While shtname = ""
'如果汇总表不存在，则建立
newsht = shtname + "汇总表"

On Error Resume Next

If Sheets(shetname) Is Nothing Then
    Sheets.Add(after:=Sheets(shtname)).Name = newsht
End If



Sheets(shtname).Activate
'定义两个字典，goods为商品名和单位键值对，goods2为商品名和价格键值对
Dim goods As New Dictionary
Dim goods2 As New Dictionary
'定义查找的单元格
Dim findrng As Range
Dim rnum, cnum As Integer
Dim goodsname
rnum = Sheets(shtname).UsedRange.Rows.Count
'去掉所有空格
Dim r As Range
For Each r In Sheets(shtname).UsedRange
    r = Replace(r, " ", "")
Next


'查找商品的名称。利用字典去重。
With Sheets(shtname).UsedRange
    Set findrng = .Find("品名", lookat:=xlWhole)
    If Not findrng Is Nothing Then
        firstaddress = findrng.Address
        
        'MsgBox "找到了，地址是" & firstaddress
    End If
    
    Do
        cnum = findrng.Column
        
        For i = 1 To rnum
            If Cells(i, cnum) <> "" And Cells(i, cnum) <> "品名" And Cells(i, cnum) <> "小计" And Cells(i, cnum).MergeCells = False Then
                Key = Cells(i, cnum)
                If Not goods.exists(Key) Then
                    goods(Key) = Cells(i, cnum).Offset(0, 1)
                    goods2(Key) = Cells(i, cnum).Offset(0, 2)
                End If
            End If
        Next
        Set findrng = .FindNext(findrng)
        'MsgBox "下一个地址是" & findrng.Address
    Loop While Not findrng Is Nothing And findrng.Address <> firstaddress
End With

'goodsname = goods.keys
'goodsprice = goods.Items

'计算各商品总数量和总金额
'Dim k As Integer
'k = 0
'k = UBound(goods.Keys) '得到商品种类数作为数组上界
Dim rng_goods As Range
Dim the_value As String

Dim totalnum()
Dim totalprice()
ReDim totalnum(0 To goods.Count)
ReDim totalprice(0 To goods.Count)



For j = 0 To UBound(goods.Keys)
    'Debug.Print goods.Keys(j)
    the_value = goods.Keys(j)
    Total = 0
    With Sheets(shtname).UsedRange
        Set rng_goods = .Find(the_value, lookat:=xlWhole)
        goods_address = rng_goods.Address
        Do
            'k = k + 1
            Total = Total + rng_goods.Offset(0, 3)
            Set rng_goods = .FindNext(rng_goods)
            
        Loop While rng_goods.Address <> goods_address
        
    End With
    totalnum(j) = Total
    totalprice(j) = Total * goods2.Items(j)
    'Debug.Print totalnum(j)
Next


'将汇总结果写入新表

Sheets(newsht).UsedRange.ClearContents
Sheets(newsht).Range("a1").Resize(1, 5) = [{"品名","单位","单价","总数量","总金额"}]
Sheets(newsht).Range("a2").Resize(goods.Count) = Application.Transpose(goods.Keys)
Sheets(newsht).Range("b2").Resize(goods.Count) = Application.Transpose(goods.Items)
Sheets(newsht).Range("c2").Resize(goods.Count) = Application.Transpose(goods2.Items)
Sheets(newsht).Range("d2").Resize(goods.Count) = Application.Transpose(totalnum())
Sheets(newsht).Range("e2").Resize(goods.Count) = Application.Transpose(totalprice())
End Sub

