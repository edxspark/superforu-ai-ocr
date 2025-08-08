

def replace_decorate_text(context: str) -> str:
    return (context.replace("```json","")
            .replace("```markdown","")
            .replace("```",""))
