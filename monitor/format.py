from chia.util.misc import format_bytes, format_minutes

def format_garis () -> str:
    return f"-----------------------------------------------"
    
def format_garis_netspace () -> str:
    return f"--------------*Netspace*--------------"
    
def format_garis_server () -> str:
    return f"----------------*Server*-----------------"
    
def format_garis_pool () -> str:
    return f"----------*FarmingStatus*----------"    
    
def format_garis_wallet () -> str:
    return f"------------------*Wallet*------------------"    
    
def format_garis_exchange () -> str:
    return f"----------*NilaiTukar-1XCH*----------"              
    
def format_og_plot_count(plot_count: int) -> str:
    return f"💿 OG Plot Count: {plot_count}"
    
def format_og_plot_size(plot_size: int) -> str:
    return f"💾 OG Plot Size: {format_bytes(plot_size)}"

def format_portable_plot_count(plot_count: int) -> str:
    return f"📀 NFT Plot Count: {plot_count}"

def format_portable_plot_size(plot_size: int) -> str:
    return f"💽 NFT Plot Size: {format_bytes(plot_size)}"

def format_plot_count(plot_count: int) -> str:
    return f"🌾 Plot Count: {plot_count}"

def format_plot_size(plot_size: int) -> str:
    return f"💽 Plot Size: {format_bytes(plot_size)}"

def format_plot_delta_24h(count_delta: int, size_delta: int) -> str:
    size_prefix = "+" if size_delta > 0 else "-"
    return f"🆕 Plot Change 24h: {count_delta:+} ({size_prefix}{format_bytes(abs(size_delta))})"

def format_balance(balance: int) -> str:
    return f"💰 Balance: {balance/1e12:.8f} XCH"

def format_farmed(balance: int) -> str:
    return f"💸 Farmed: {balance/1e12:.8f} XCH"
    
def format_balance_idr(balance_idr: int) -> str:
    balance_idr_ribuan = f"{balance_idr:,}"
    return f"💸 est. IDR: {balance_idr_ribuan}"    

def format_space(space: int) -> str:
    return f"🌏 Net Size: {format_bytes(space)}"

def format_diffculty(difficulty: int) -> str:
    return f"📈 Net Diff: {difficulty}"

def format_peak_height(peak_height: int, fix_indent=False) -> str:
    indent = " " * (1 if fix_indent else 0)
    return f"🏔️ {indent}Peak Height: {peak_height}"

def format_synced(synced: int) -> str:
    return f"🔄 Synced: {synced}"

def format_full_node_count(full_node_count: int, node_type="Full Node") -> str:
    return f"📶 {node_type} Count: {full_node_count}"
    
def format_harvester(full_node_count: int, node_type="Harvester") -> str:
    return f"🖥️ {node_type} Count: {full_node_count}"

def format_hostname(hostname: str, fix_indent=False) -> str:
    indent = " " * (1 if fix_indent else 0)
    return f"🖥️ {indent}Host: {hostname}"

def format_challenge_hash(challenge_hash: str) -> str:
    return f"🎰 Challenge Hash: {challenge_hash}"

def format_challenges_per_min(challenges_per_min: float) -> str:
    return f"🎰 Challenges Per Minute: {challenges_per_min:.2f}"

def format_signage_point(signage_point: str) -> str:
    return f"⌛ Signage Point: {signage_point}"

def format_signage_points_per_min(signage_points_per_min: float) -> str:
    return f"⌛ Signage Per Minute: {signage_points_per_min:.2f}"

def format_signage_point_index(signage_point_index: int) -> str:
    return f"🔏 Signage Point Index: {signage_point_index}"

def format_passed_filter(passed_filter: int) -> str:
    return f"🔎 Passed Filter: {passed_filter}"

def format_passed_filter_per_min(passed_filter_per_min: float) -> str:
    return f"🔎 Passed Per Minute: {passed_filter_per_min:.2f}"

def format_proofs(proofs: int) -> str:
    return f"🆗 Total Proofs found: {proofs}"

def format_proofs_per_hour(proofs_per_hour: float) -> str:
    return f"✅ Proofs last 1h: {proofs_per_hour}"
    
def format_proofs_24h(proofs_per_24h: float) -> str:
    return f"☑️ Proofs last 24h: {proofs_per_24h}"    

def format_expected_time_to_win(minutes: int) -> str:
    return f"🕰️ Time To Win: {format_minutes(minutes)}"

def format_current_points(points: int) -> str:
    return f"🟣 Current Points: {points}"

def format_pool_difficulty(difficulty: int) -> str:
    return f"📈 Pool Difficulty: {difficulty}"

def format_points_found(points: int) -> str:
    return f"🟡 Point Since Start: {points}"

def format_points_acknowledged(points: int) -> str:
    return f"🟠 Point Acknowledged: {points}"

def format_points_found_24h(points: int) -> str:
    return f"🟢 Point Last 24h: {points}"

def format_points_acknowledged_24h(points: int) -> str:
    return f"🔵 Point Acknowledged Last 24H: {points}"

def format_pool_errors_24h(errors: int) -> str:
    return f"❌ Point Errors 24h: {errors}"

def format_price(amount: int, currency: str, fix_indent=False) -> str:
    indent = " " * (1 if fix_indent else 0)
    return f"🏷️ {indent}Price in {currency}: {amount}"

def format_usd(amount: int) -> str:
    return f"💵 Price in USD: {amount/1e2:.2f}"
    
def format_euro(amount: int) -> str:
    return f"💶 Price in EUR: {amount/1e2:.2f}"
    
def format_idr(amount: int) -> str:
    ribuan = f"{amount:,}"
    return f"💷 Price in IDR: {ribuan}"

def format_btc(amount: int) -> str:
    return f"🪙 Price in BTC: {amount/10e7}" 
    
def format_eth(amount: int) -> str:
    return f"🪙 Price in ETH: {amount/10e8}"       
