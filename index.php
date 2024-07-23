<?php

error_reporting(0);
session_start();
header('Content-Type: application/json');

// Hàm để trả về JSON
function ECHOJSON($data) {
    echo json_encode($data);
    exit;
}

// Kiểm tra giá trị 'count' trong yêu cầu GET
if (isset($_GET["count"]) && $_GET["count"] > 0) {
    $count = (int)$_GET["count"];

    // Nếu count lớn hơn 3, trả về thông báo lỗi
    if ($count > 3) {
        ECHOJSON(array("status" => "error", "msg" => "Count 3 = Max nha"));
    }

    // Log thông tin sdt và count
    if (isset($_GET["sdt"])) {
        $sdt = $_GET["sdt"];
    } else if (isset($_POST["sdt"])) {
        $sdt = $_POST["sdt"];
    } else {
        ECHOJSON(array("status" => "error", "msg" => "VUI LÒNG REQUESTS CÓ SDT"));
    }

    // Kiểm tra sdt không hợp lệ
    if (in_array($sdt, ["113", "114", "115", "911"])) {
        ECHOJSON(array("status" => "error", "msg" => "spam so nay con me may a` ???"));
    }

    error_log("sdt = " . $sdt . " count = " . $count . " Accepted");

    // Kiểm tra độ dài số điện thoại
    if (strlen($sdt) < 10) {
        ECHOJSON(array("status" => "error", "msg" => "Vui Lòng Nhập Đúng Số SDT"));
    } else if (!$sdt) {
        ECHOJSON(array("status" => "error", "msg" => "Vui Lòng Nhập Đúng Số SDT"));
    } else {
        // Đường dẫn tuyệt đối đến script.py trên Replit
        $scriptPath = "/home/runner/th1nksms/script.py";
        
        // Chạy script Python
        $command = escapeshellcmd("python3 $scriptPath {$sdt} {$count}");
        $output = shell_exec($command);

        // Kiểm tra xem lệnh có chạy thành công hay không
        if ($output === null) {
            ECHOJSON(array("status" => "error", "msg" => "Lỗi khi chạy source spam python"));
        } else {
            // Trả về đầu ra từ script Python dưới dạng JSON
            ECHOJSON(array("status" => "success", "msg" => "Thành Công, Api: 64", "output" => $output));
        }
    }
} else {
    ECHOJSON(array("status" => "error", "msg" => "Số lượng không hợp lệ"));
}

?>
