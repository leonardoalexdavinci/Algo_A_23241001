import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // deklarasi variabel dan tipe data 
        String nama;
        int nim;
        String prodi;
        double tinggi_badan;

        //membuat scanner baru
        Scanner input = new Scanner (System.in);

        System.out.println("Form Data Mahasiswa UNDIKMA");
        System.out.println("===========================");
        // membuat Form
        System.out.print("Masukan Nama Mahasiswa : ");
        nama = input.nextLine();

        System.out.print("Masukan Prodi : ");
        prodi = input.nextLine();

        System.out.print("Masukan NIM : ");
        nim = input.nextInt();

        System.out.print("Masukan Tinggi Badan : ");
        tinggi_badan = input.nextDouble();

        //cetak output ke layar monitor
        System.out.println("Data Mahasiswa UNDIKMA");
    }
}
