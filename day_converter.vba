Function DayOfYearAlways366(dateValue As Date) As Integer
    Dim year As Integer
    Dim isLeapYear As Boolean
    Dim dayOfYear As Integer
    
    year = Year(dateValue)
    isLeapYear = (year Mod 4 = 0 And (year Mod 100 <> 0 Or year Mod 400 = 0))
    dayOfYear = dateValue - DateSerial(year, 1, 1) + 1
    
    If Not isLeapYear And Month(dateValue) > 2 Then
        dayOfYear = dayOfYear + 1
    End If
    
    DayOfYearAlways366 = dayOfYear
End Function
