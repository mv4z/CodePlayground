/*
Martin Vazquez
CSC 355 Section 501
Assignment 7 Problem Number1
March 11, 2020
*/
declare
	a WITHHOLD.Rate1%type;
	b WITHHOLD.Rate2%type;
	c WITHHOLD.Threshold%type;

	payInfo PAYROLL%rowtype;
	netPay PAYROLL.ESalary%type;
    taxWithheld netPay%type;
    totalTax taxWithheld%type := 0;

	cursor payrollPtr is SELECT * FROM PAYROLL;

begin
	select Rate1, Rate2, Threshold
	INTO a, b, c
	FROM withhold;
    
	DBMS_OUTPUT.PUT_LINE('Rates : ' || a || ', ' || b);
	DBMS_OUTPUT.PUT_LINE('Threshold : ' || c);
    DBMS_OUTPUT.PUT_LINE('');

	for payInfo in payrollPtr
	loop
		if payInfo.ESalary <= c then
            taxWithheld := (payInfo.ESalary * (a/100));
			netPay := payInfo.ESalary - taxWithheld;
			DBMS_OUTPUT.PUT_LINE(payInfo.EID || ': ' || payInfo.ESalary || ' ' || taxWithheld || ' '|| netPay );
            totalTax := totalTax + taxWithheld;
		else
            taxWithheld := (c * (a/100)) + ((payInfo.ESalary - c) *(b/100));
            netPay := payInfo.ESalary - taxWithheld;
			DBMS_OUTPUT.PUT_LINE(payInfo.EID || ': ' || payInfo.ESalary || ' ' || taxWithheld || ' '|| netPay );
            totalTax := totalTax + taxWithheld;
        end if;

	end loop;
    DBMS_OUTPUT.PUT_LINE('');
    DBMS_OUTPUT.PUT_LINE('Total Tax: ' || totalTax );
    
end;
