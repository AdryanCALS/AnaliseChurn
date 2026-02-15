--select c.customerID  from Clients c where c.Churn = "Yes" --Selecionando os Clientes que fizeram o cancelamento por ID

--SELECT COUNT(c.customerID) as QTD_CHURN from Clients c where c.Churn = "Yes" --Fazendo a contagem

/*SELECT 
	COUNT(*) as total_clientes,
	AVG(case when c.Churn = "Yes" then 1 else 0 end) as taxa_churn
from Clients c;*/ --Porcentagem de churn do DataSet

--SELECT avg(c.MonthlyCharges) as Media_Mensalidade FROM Clients c -- -Vendo o preço médio da Mensalidade que é cobrado

--SELECT c.InternetService as Tipo_Internet, COUNT(c.InternetService) as QTD FROM Clients c GROUP BY c.InternetService-- Vendo os tipos de plano de internet

/*SELECT
    c.Churn,
    AVG(c.MonthlyCharges) as Media_Mensalidade
FROM
    Clients c
GROUP BY
    c.Churn;*/ -- analisando a mensalidade de pessoas que fizeram ou n churn