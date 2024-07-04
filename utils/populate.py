""" Populate the database with some data at the start of the application"""

from src.persistence.repository import Repository


def populate_db(repo: Repository) -> None:
	"""Populates the db with a dummy country"""
	from src.models.country import Country

	try:
		countries = [
			Country(name="Uruguay", code="UY"),
			Country(name="Argentina", code="AR"),
			Country(name="Brazil", code="BR"),
			Country(name="Chile", code="CL"),
			Country(name="Paraguay", code="PY"),
			Country(name="Bolivia", code="BO"),
			Country(name="Peru", code="PE"),
			Country(name="Ecuador", code="EC"),
			Country(name="Colombia", code="CO"),
			Country(name="Venezuela", code="VE"),
			Country(name="Guyana", code="GY"),
			Country(name="Suriname", code="SR"),
			Country(name="French Guiana", code="GF"),
			Country(name="Panama", code="PA"),
			Country(name="Costa Rica", code="CR"),
			Country(name="Nicaragua", code="NI"),
			Country(name="Honduras", code="HN"),
			Country(name="El Salvador", code="SV"),
			Country(name="Guatemala", code="GT"),
			Country(name="Belize", code="BZ"),
			Country(name="Mexico", code="MX"),
			Country(name="Cuba", code="CU"),
			Country(name="Jamaica", code="JM"),
			Country(name="Haiti", code="HT"),
			Country(name="Dominican Republic", code="DO"),
			Country(name="Puerto Rico", code="PR"),
		]

		for country in countries:
			existing_country = repo.get_by_code(Country, country.code)
			if existing_country is None:
				repo.save(country)

		print("Memory DB populated")

	except ImportError:
		print("No more countries to add")
