select departement.nom as Departamento, employee.nom as Empregado, round(sum(salaire.salaire)/2,2) as "Salario Bruto",
reductionSalaire.redSalaire as "Total Desconto"
from 
(
	select empregado.lotacao as codeDepartement, departamento.nome as nom
	from empregado, departamento
	where empregado.lotacao = departamento.cod_dep
	group by codeDepartement, nom
) as departement,
(
	select empregado.matr as matricule, empregado.nome as nom, empregado.lotacao as codeDepartement
	from empregado
) as employee,
(
	select empregado.matr as matricule, vencimento.valor as salaire
	from empregado, vencimento, emp_venc
	where
	vencimento.cod_venc = emp_venc.cod_venc
	and empregado.matr = emp_venc.matr
	group by empregado.matr, vencimento.valor
) as salaire,
(
	select empregado.matr as matricule, coalesce(desconto.valor, 0) as redSalaire
	from desconto, emp_dec
	right join empregado on empregado.matr = emp_desc.matr
) as reductionSalaire
where
	employee.codeDepartement = departement.codeDepartement
	and salaire.matricule = employee.matricule
	and reductionSalaire.matricule = employee.matricule
	group by departement.nom, employee.nom, reductionSalaire.redSalaire
