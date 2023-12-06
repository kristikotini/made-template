from typing import Any, Optional, NamedTuple


class ParameterizationStruct(NamedTuple):
    input: Any
    output: Any
    description: Optional[str] = None


def validate_column_choices(df, column, choices):
    """
    Validate that all values in the specified column are within the given choices.
    """
    return df[column].isin(choices).all()


STATE_NAMES = [
    'Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
    'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland',
    'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen'
]

PLACE_NAMES = ['inner town', 'out of town (without motorways)', 'on highways', 'In total']

SEVERITY_NAMES = ['Killed', 'Seriously injured', 'Slightly injured', 'In total']
