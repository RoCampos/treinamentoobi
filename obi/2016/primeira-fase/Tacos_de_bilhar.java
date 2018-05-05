
// https://olimpiada.ic.unicamp.br/pratique/p1/2016/f1/tacos-bilhar/

import java.util.Scanner;

public class Tacos_de_Bilhar{

	public static void main(String[] args) {

		Scanner sc = new Scanner (System.in);
		int C = sc.nextInt();
		int [] cue_size = new int[1000000];
		int count = 0;
		for (int i =0; i < C; i++) {
			
			int cues = sc.nextInt ();
			
			if (cue_size[cues] == 0) {
				count += 2;
				cue_size[cues] = 1;
			} else {
				cue_size[cues] = 0;
			}

		}	
		System.out.println (count);
	}
	
}