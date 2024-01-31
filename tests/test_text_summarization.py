import sys
print(sys.path)
sys.path.append('../')
print(sys.path)


from pdf_processing.preprocessing import summarize_text

input_text = """Love encompasses a range of strong and positive emotional and mental states, from the most sublime virtue or good habit, the deepest interpersonal affection, to the simplest pleasure.[1] An example of this range of meanings is that the love of a mother differs from the love of a spouse, which differs from the love for food. Most commonly , love refers to a feeling of strong attraction and emotional attachment.[2] Love is considered to be both positive and negative, with its virtue representing human kindness, compassion, and affection—"the unselfish, loyal and benevolent concern for the good of another"—and its vice representing a human moral flaw akin to vanity , selfishness, amour-propre, and egotism, potentially leading people into a type of mania, obsessiveness, or codependency .[3] It may also describe compassionate and affectionate actions towards other humans, oneself, or animals.[4] In its various forms, love acts as a major facilitator of interpersonal relationships and, owing to its central psychological importance, is one of the most common themes in the creative arts.[5][6] Love has been postulated to be a function that keeps human beings together against menaces and to facilitate the continuation of the species.[7]"""
result_summary = summarize_text(input_text)
expected_summary = """Most commonly , love refers to a feeling of strong attraction and emotional attachment. [3] It may also describe compassionate and affectionate actions towards other humans, oneself, or animals. [4] In its various forms, love acts as a major facilitator of interpersonal relationships and, owing to its central psychological importance, is one of the most common themes in the creative arts."""
assert result_summary == expected_summary