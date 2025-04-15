import tkinter as tk

root = tk.Tk()
root.configure(bg='lightblue')
root.title('Sunday Cipher Decryption')
root.geometry('400x300')
text_label = tk.Label(root, text='Enter cipher text (Two or more numbers, maxium 6)',bg='lightblue', fg='black')
text_label.pack()
text_in = tk.Entry(root, width=20)
text_in.pack(pady=5)
button = tk.Button(root, text='Decrypt',bg='lightblue', fg='black')
button.pack(pady=5)

root.mainloop()