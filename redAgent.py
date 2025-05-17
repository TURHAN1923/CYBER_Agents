# red_team_agent.py
from mistral_api import ask_ollama


def red_team_attack(system_info):
    try:
        prompt = f"""
Sen bir Red Team güvenlik uzmanısın.
Aşağıdaki sistem bilgilerine göre sızma testi yap ve saldırı planı öner:

Sistem Bilgileri:
{system_info}

1. Hangi saldırılar uygulanabilir?
2. Hangi araçlar ve yöntemler kullanılabilir?
3. Saldırı planını adım adım belirt.
"""
        result = ask_ollama(prompt)

        if not result.strip():
            return "❗ LLM yanıtı boş döndü. Lütfen daha fazla detaylı sistem bilgisi girin."

        return result

    except Exception as e:
        return f"❌ HATA: LLM sorgusu başarısız oldu.\nHata mesajı: {str(e)}"


if __name__ == "__main__":
    info = input("Sistem bilgilerini giriniz:\n> ")
    print("\n🔴 Red Agent çıktısı:\n")
    print(red_team_attack(info))
