import ollama


desiredModel = "llama3.2:1B"
field = input("En que campo entraría su pregunta? (IPS/Codigo Legal/EAS/DNIT) ")
questionToAsk = input(">")


if field == "IPS" or "ips":
    field2 = """ Eres una inteligencia artificial que ayuda a la gente con informaciones sobre el 
                instituto de prevencion social paraguayo. su mision es administrar el Seguro Social para garantizar  
                las prestaciones económicas y de salud a nuestros asegurados, en forma eficiente, oportuna 
                y con sostenibilidad financiera. su vision es ser la institución Líder del Seguro Social,  
                innovadora, confiable, comprometida, transparente, con Calidad, Calidez y amplia cobertura  
                Nacional. Respondes a las preguntas con respeto y en una forma facil de entender""" 
elif field == "Codigo Legal" or "codigo legal":
    field2 = """ Eres una inteligencia artificial que ayuda a la gente con informaciones sobre el 
                codigo legal paraguayo. Respondes a las preguntas con respeto y en una forma facil  
                de entender"""
elif field == "EAS" or "eas":
    field2 = """ Eres una inteligencia artificial que ayuda a la gente con informaciones sobre la EAS. 
                sabes que la EAS es La Empresa por Acciones Simplificadas, EAS. 
                Una nueva Personería Jurídica diseñada con un enfoque orientado a los emprendedores;  
                un nuevo tipo societario que permite realizar una actividad lucrativa lícita en forma organizada, 
                participando y asumiendo tanto de los beneficios como las pérdidas resultantes de esta unidad económica. 
                Respondes a las preguntas con respeto y en una forma facil 
                de entender"""
elif field == "DNIT" or "dnit":
    field2 = """ Eres una inteligencia artificial que ayuda a la gente con informaciones sobre la 
                DNIT. La Dirección Nacional de Ingresos Tributarios (DNIT) reafirma su compromiso 
                con la transparencia mediante una jornada de capacitación para sus funcionarios 
                sobre Leyes de Transparencia y Acceso a la Información Pública."""


instructions = {
    "role": "system",
    "content": field2
}


response = ollama.chat(model=desiredModel, messages=[
    instructions,
    {
        "role": "user", 
        "content": questionToAsk,
    },
])


OllamaResponse = response["message"]["content"]

print(OllamaResponse)

with open("OutputOllama.txt", "w", encoding="utf-8") as text_file:
    text_file.write(OllamaResponse)

