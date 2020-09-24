let Prelude = https://prelude.dhall-lang.org/package.dhall

let groups = Prelude.List.generate 24 Text
	(\(n : Natural) -> "ИКБО-${Natural/show (n + 1)}-19")

let addStudent =
	\(age : Natural) ->
	\(group : Natural) ->
	\(name : Text) ->
	{
		age = age,
		group = "ИКБО-${Natural/show group}-19",
		name = name
	}

let students = [
	addStudent 19 4 "Иванов И.И.",
	addStudent 18 5 "Петров П.П.",
	addStudent 18 5 "Сидоров С.С.",
	addStudent 19 1 "Акимов В.Е."
]

let subject = "Конфигурационное управление"

in {students, groups, subject}