def get_user_info():
    """Kullanıcının adını, yaşını ve favori programlama dilini alır."""
    name = input("Lütfen adınızı girin: ")
    age = int(input("Lütfen yaşınızı girin: "))
    print("Favori programlama dilinizi seçin:")
    print("1. Python")
    print("2. JavaScript")
    print("3. Java")
    print("4. C++")
    print("5. Diğer")
    language_choice = input("Seçiminiz (1-5): ")
    
    return name, age, language_choice

def get_hello_world_message(language_choice):
    """Seçilen programlama diline göre 'Hello, World!' mesajını döner."""
    messages = {
        '1': 'print("Hello, World!")  # Python',
        '2': 'console.log("Hello, World!");  // JavaScript',
        '3': 'System.out.println("Hello, World!");  // Java',
        '4': 'std::cout << "Hello, World!" << std::endl;  // C++',
        '5': 'Hello, World!  // Diğer'
    }
    return messages.get(language_choice, 'Hello, World!  // Bilinmeyen dil')

def age_based_message(age):
    """Kullanıcının yaşına göre özel bir mesaj döner."""
    if age < 18:
        return "Sen genç ve heveslisin! Kodlamaya başlamak için harika bir yaş."
    elif 18 <= age < 30:
        return "Genç ve dinamik! Yeni teknolojilere açık ol."
    elif 30 <= age < 50:
        return "Tecrübe ve bilgi birikimiyle daha güçlü kodlama!"
    else:
        return "Bilgelik yaşla gelir. Tecrübeleriniz kodlarınıza yansıyacak!"

def main():
    """Programın ana fonksiyonu."""
    name, age, language_choice = get_user_info()
    hello_world_message = get_hello_world_message(language_choice)
    special_message = age_based_message(age)
    
    print(f"\nMerhaba, {name}! İşte senin için özel mesajlar:")
    print(hello_world_message)
    print(special_message)

if __name__ == "__main__":
    main()

